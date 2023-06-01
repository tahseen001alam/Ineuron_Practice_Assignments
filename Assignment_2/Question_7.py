l=list(map(int,input().split()))
k=1
for i in range(len(l)-1):
    if abs(l[i]-l[i+1])==0 or abs(l[i]-l[i+1])==1:
        continue
    else:
        k=0
        break
if k==1:
    print("true")
else:
    print("false")
