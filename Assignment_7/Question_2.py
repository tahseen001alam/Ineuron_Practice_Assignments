def icc(num):
    s_pair = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    l, r = 0, len(num) - 1

    while l <= r:
        if num[l] not in s_pair or num[r] != s_pair[num[l]]:
            return False
        l += 1
        r -= 1

    return True

num=input()
print(icc(num))

