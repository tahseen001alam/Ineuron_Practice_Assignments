def mdf(nums, k):
    min_num = float('inf')
    max_num = float('-inf')

    for num in nums:
        min_num = min(min_num, num)
        max_num = max(max_num, num)

    if min_num + k >= max_num - k:
        return 0

    return max_num - k - (min_num + k)
nk=list(map(int,input().split()))
hk=int(input())
print(mdf(nk,hk))
