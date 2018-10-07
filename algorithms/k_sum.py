def KSum(nums, target, _N):
    results = []
    stack = []

    def findKsum(nums, target, N):
        # early termination
        if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:
            return
        if N == 2:  # two pointers solve sorted 2-sum problem
            l, r = 0, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append(stack + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        else:  # recursively reduce N
            for i in range(len(nums) - N + 1):
                # avoid duplication
                if i == 0 or nums[i - 1] != nums[i]:
                    stack.append(nums[i])
                    findKsum(nums[i + 1:], target - nums[i], N - 1)
                    stack.pop()

    findKsum(sorted(nums), target, _N)
    return results


results = KSum([1, 0, -1, 0, -2, 2], 0, 4)
print(results)
