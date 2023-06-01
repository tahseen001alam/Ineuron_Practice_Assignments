def get(no,tar):
    l=0
    r=len(tar)-1
    while l<=r:
        mid=(l+r)//2
        if tar[mid]==no:
            return mid
        elif tar[mid]<no:
            l=mid+1
        else:
            r=mid-1
    return -1
tar=list(map(int,input().split()))
no=int(input())
print(get(no,tar))
