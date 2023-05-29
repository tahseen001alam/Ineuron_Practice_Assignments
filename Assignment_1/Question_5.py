
def merge(n1, mm, n2, n):
    p1 = mm - 1  
    p2 = n - 1  
    p = mm + n - 1  

    while p1 >= 0 and p2 >= 0:
        if n1[p1] > n2[p2]:
            n1[p] = n2[p1]
            p1 -= 1
        else:
            n1[p] = n2[p2]
            p2 -= 1
        p -= 1

    while p2 >= 0:
        n1[p] = n2[p2]
        p2 -= 1
        p -= 1

n1 = list(map(int,input().split()))
mm = int(input())
n2 = list(map(int,input().split()))
n = int(input())

merge(n1, mm, n2, n)
print(n1)
