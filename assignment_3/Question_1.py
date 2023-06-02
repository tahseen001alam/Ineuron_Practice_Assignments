def tsc(nums, t):
    n = len(nums)
    nums.sort()
    csum = float('inf')

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if abs(current_sum - t) < abs(csum - t):
                csum = current_sum

            if current_sum < t:
                left += 1
            elif current_sum > t:
                right -= 1
            else:
                return csum

    return csum

nums=list(map(int,input().split()))
t=int(input())
print(tsc(nums,t))





