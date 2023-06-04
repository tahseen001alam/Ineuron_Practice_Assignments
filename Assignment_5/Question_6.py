def fd(nu):
    re = []
    for num in nu:
        ind = abs(num)
        if nu[ind - 1] > 0:
            nu[ind - 1] *= -1
        else:
            re.append(ind)
    return re
lk=list(map(int,input().split()))
print(fd(lk))