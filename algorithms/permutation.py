def unique_permutation(arr):
    res = [[]]
    for n in arr:
        new_res = []
        for sub_arr in res:
            # for each sub_arr, we split it into two at a given position i and concatenate with the curr n
            for i in range(len(sub_arr) + 1):
                new_res.append(sub_arr[:i] + [n] + sub_arr[i:])
                # avoid inserting n right next to another n
                if i < len(sub_arr) and sub_arr[i] == n:
                    break
        res = new_res
        print(res)
    return res


vec = [1, 2, 1, 1]
# should print: [[2, 1, 1], [1, 2, 1], [1, 1, 2]]
print(unique_permutation(vec))
