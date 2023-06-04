def gets(nums):
    l = 0
    r = len(nums) - 1
    re = []

    while l <= r:
        if abs(nums[l]) >= abs(nums[r]):
            re.append(nums[l] ** 2)
            l += 1
        else:
            re.append(nums[r] ** 2)
            r -= 1

    return re[::-1]

lk=list(map(int,input().split()))
print(gets(lk))
