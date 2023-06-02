def sn(l):
    result = 0
    for i in l:
        result ^= i
    return result
l=list(map(int,input().split()))
print(sn(l))