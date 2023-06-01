f=list(map(int,input().split()))
n=int(input())
l=len(f)
i=0
count=0
while i < len(f):
        if f[i] == 0 and (i == 0 or f[i-1] == 0) and (i == l-1 or f[i+1] == 0):
            f[i] = 1
            count += 1
        i += 1
if count>=n:
    print("true")
else:
    print("false")
