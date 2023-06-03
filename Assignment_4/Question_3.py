n1=int(input())
n2=int(input())
mat=[]
for i in range(n1):
    a=[]
    for j in range(n2):
        a.append(int(input()))
    mat.append(a)
#print(mat)
kat=[[0 for i in range(n1)] for j in range(n2)]
for i in range(n1):
    for j in range(n2):
        kat[j][i]=mat[i][j]
print(kat)
        
