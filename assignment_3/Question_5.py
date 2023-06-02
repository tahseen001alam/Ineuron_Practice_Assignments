def pO(d):
    carry = 1
    for i in range(len(d) - 1, -1, -1):
        d[i] += carry
        carry = d[i] // 10
        d[i] %= 10
        if carry == 0:
            break

    if carry != 0:
        d.insert(0, carry)

    return d
d=list(map(int,input().split()))
print(pO(d))