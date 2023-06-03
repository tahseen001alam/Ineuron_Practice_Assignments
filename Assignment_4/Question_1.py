ar1=list(map(int,input().split()))
ar2=list(map(int,input().split()))
ar3=list(map(int,input().split()))
kl=[]
for i in range(len(ar1)):
    if ar1[i] in ar2 and ar1[i] in ar3:
        kl.append(ar1[i])
kl.sort()
print(kl)
