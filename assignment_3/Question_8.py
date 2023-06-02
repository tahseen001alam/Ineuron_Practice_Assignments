
n1=int(input())
n2=int(input())
pk=0
mat=[]
for i in range(n1):
    a=[]
    for j in range(n2):
        a.append(int(input()))
    mat.append(a)
mat.sort(key=lambda x:x[0])
for i in range(1,len(mat)):
    if mat[i][0]<mat[i-1][1]:
        print("false")
    else:
        pk+=1
if pk==(n1*n2)//2:
    print("True")


