#include <iostream>
#include <unordered_map>
#include <map>
#include <list>

using namespace std;

class LFUCache {
	int capacity;
	unordered_map<int, pair<int, list<pair<int, int>>::iterator>> mp; // key -> (freq, iterator of (key, value))
	map<int, list<pair<int, int>>> fmap; // freq -> list of (key, value)
	
public:
	LFUCache(int capacity) : capacity(capacity) {}
	
	list<pair<int, int>>::iterator getIterator(int key){
		int f = mp[key].first++;
		fmap[f+1].splice(fmap[f+1].end(), fmap[f], mp[key].second);
		if(fmap[f].empty()) fmap.erase(f);
		return mp[key].second;
	}
	
	int get(int key) {
		return mp.count(key) ? getIterator(key)->second : -1;
	}
	
	void put(int key, int value) {
		if(capacity<1) return;
		else if(mp.count(key)) getIterator(key)->second = value;
		else{
			if(mp.size()==capacity){
				mp.erase(fmap.begin()->second.front().first);
				fmap.begin()->second.pop_front();
				if (fmap.begin()->second.empty()) fmap.erase(fmap.begin());
			} 
			fmap[1].push_back({key, value});
			mp[key] = {1, prev(fmap[1].end())};   
		}
	}
};


using namespace std;
int main(int argc, char *argv[]) {
	auto cache = LFUCache(3);
	cache.put(1, 1);
	cache.put(2, 2);
	cache.put(3, 3);
	cache.get(1);
	cache.get(1);
	cache.put(4, 4);
	cache.put(5, 5);
	for(int i=1; i<6; i++)
		cout << cache.get(i) << ' ';
	cout << endl;
}
