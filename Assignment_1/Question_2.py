def searchInsert(nums, tar):
    l = 0
    r = len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        
        if nums[mid] == tar:
            return mid
        elif nums[mid] < tar:
            l = mid + 1
        else:
            r = mid - 1
    
    return l

nums = list(map(int,input().split()))
tar = int(input())
result = searchInsert(nums, tar)
print(result)
