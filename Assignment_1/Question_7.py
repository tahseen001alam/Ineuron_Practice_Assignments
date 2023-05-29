
def move(n):
    l = 0

    for r in range(len(n)):
        if n[r] != 0:
            n[l], n[r] = n[r], n[l]
            l += 1

n = list(map(int,input().split()))
move(n)
print(n)
