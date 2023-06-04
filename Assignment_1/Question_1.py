'''def twoSum(nums, tar):
    d = {}  
    
    for i, num in enumerate(nums):
        complement = tar - num
        
        
        if complement in d:
            return [d[complement], i]
        
        d[num] = i
    
    return []

nums = list(map(int,input().split()))
tar = int(input())
result = twoSum(nums, tar)
print(result)'''

def func(s):

    if len(s) <= 1:
        return s

    return func(s[ 2 : ]) + s[0]
print(func("AeI123"))