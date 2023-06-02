def sii(nums, t):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == t:
            return mid
        elif nums[mid] < t:
            left = mid + 1
        else:
            right = mid - 1

    return left
nums=list(map(int,input().split()))
t=int(input())
print(sii(nums,t))