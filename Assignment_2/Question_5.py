n=list(map(int,input().split()))
n.sort()
print(max(n[len(n)-1]*n[len(n)-2]*n[len(n)-3],n[0]*n[1]*n[len(n)-1]))
