n=list(map(int,input().split()))
n.sort()
maxx_s=0
for i in range(0,len(n),2):
    maxx_s+=min(n[i],n[i+1])
print(maxx_s)













