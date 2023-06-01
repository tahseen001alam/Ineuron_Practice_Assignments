from collections import defaultdict

def get(nums):
    co = defaultdict(int)
    for num in nums:
        co[num] += 1

    maxLen = 0
    for num in co:
        if num + 1 in co:
            currLen = co[num] + co[num + 1]
            maxLen = max(maxLen, currLen)

    return maxLen

l=list(map(int,input().split()))
print(get(l))