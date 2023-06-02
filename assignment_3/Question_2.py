def fourSum(nums, target):
    n = len(nums)
    nums.sort()
    result = []

    def findQuadruplets(nums, target, start, current, result):
        if len(current) == 4:
            if sum(current) == target:
                result.append(current[:])
            return

        if len(current) > 4 or start >= len(nums):
            return

        for a in range(start, n - 3):
            if a > start and nums[a] == nums[a - 1]:
                continue

            current.append(nums[a])
            findQuadruplets(nums, target, a + 1, current, result)
            current.pop()

    findQuadruplets(nums, target, 0, [], result)
    return result

