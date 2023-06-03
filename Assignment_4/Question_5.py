n=int(input())
i=1
co=[]
while(n):
    if i>n:
        break
    else:
        co.append(i)
        n=n-i
        i+=1
print(len(co))
