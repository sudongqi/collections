import random


def quickselect(vec, k):
    def dfs(l, r):
        # base case
        if r == l:
            return vec[l]
        # choose random pivot
        pivot_index = random.randint(l, r)
        # move pivot to beginning of list
        vec[l], vec[pivot_index] = vec[pivot_index], vec[l]

        # partition
        i = l
        for j in range(l + 1, r + 1):
            if vec[j] < vec[l]:
                i += 1
                vec[i], vec[j] = vec[j], vec[i]
        # move pivot to correct location
        vec[i], vec[l] = vec[l], vec[i]

        # recursively partition one side only
        if k == i:
            return vec[i]
        elif k < i:
            return dfs(l, i - 1)
        else:
            return dfs(i + 1, r)

    if vec is None or len(vec) < 1:
        return None
    if not 0 <= k < len(vec):
        raise IndexError()
    return dfs(0, len(vec) - 1)


vec = list(range(10))
random.shuffle(vec)
for i in range(len(vec)):
    print(quickselect(vec, i), end=' ')
