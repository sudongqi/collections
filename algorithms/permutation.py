def unique_permutation(arr):
    res = [[]]
    for n in arr:
        new_res = []
        for sub_arr in res:
            for i in range(len(sub_arr) + 1):
                # insert n into the partially completed array
                new_res.append(sub_arr[:i] + [n] + sub_arr[i:])
                # avoid inserting n right next to another n
                if i < len(sub_arr) and sub_arr[i] == n:
                    break
        res = new_res
    return res


vec = [1, 1, 2]
# should print: [[2, 1, 1], [1, 2, 1], [1, 1, 2]]
print(unique_permutation(vec))
