
def removeElement(n, v):
    k = 0  

    for i in range(len(n)):
        if n[i] != v:
            n[k] = n[i]
            k += 1

    return k

n = list(map(int,input().split()))
v = int(input())
result = removeElement(n, v)
print(result)
print(*n[:result])
