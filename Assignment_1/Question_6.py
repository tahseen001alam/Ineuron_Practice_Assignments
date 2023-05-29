def containsDup(n):
    se_e_n = set()

    for num in n:
        if num in se_e_n:
            return True
        se_e_n.add(num)

    return False

n =list(map(int,input().split()))
print(containsDup(n))
