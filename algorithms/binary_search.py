def bisect_left(nums, target):
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


def bisect_right(nums, target):
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left


res0 = bisect_left([1, 2, 2, 2, 3, 9], 2)
res1 = bisect_left([1, 2, 2, 2, 3, 9], 2.1)
res2 = bisect_right([1, 2, 2, 2, 3, 9], 2)
res3 = bisect_right([1, 2, 2, 2, 3, 9], 2.1)

# 1, 4, 4, 4
print(res0, res1, res2, res3)
