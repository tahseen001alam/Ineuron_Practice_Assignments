li1=list(map(int,input().split()))
li2=list(map(int,input().split()))
get1=[]
for i in range(len(li1)):
    if li1[i] not in li2:
        get1.append(li1[i])
get1=sorted(set(get1))
get2=[]
for i in range(len(li2)):
    if li2[i] not in li1:
        get2.append(li2[i])

get2=sorted(set(get2))

print([get1,get2])
