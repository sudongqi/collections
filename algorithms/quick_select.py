import random


def quick_select(items, k):
    if items is None or len(items) < 1:
        return None

    def select(lst, l, r, index):
        if l == r:
            return lst[l]
        pivot_index = random.randint(l, r)
        lst[l], lst[pivot_index] = lst[pivot_index], lst[l]

        i = l
        for j in range(l + 1, r + 1):
            if lst[j] < lst[l]:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[i], lst[l] = lst[l], lst[i]

        if index == i:
            return lst[i]
        elif index < i:
            return select(lst, l, i - 1, index)
        return select(lst, i + 1, r, index)

    return select(items, 0, len(items) - 1, max(0, min(k, len(items) - 1)))


vec = list(range(10))
random.shuffle(vec)
for i in range(len(vec)):
    print(quick_select(vec, i), end=' ')
