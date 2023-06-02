def fmr(l, lo, up):
    result = []
    start = lo

    for num in l:
        if num <= start:
            continue

        if num > start:
            missing_range = [start, num - 1]
            result.append(missing_range)

        start = num + 1

    if start <= up:
        missing_range = [start, up]
        result.append(missing_range)

    return result
l=list(map(int,input().split()))
lo=int(input())
up=int(input())
print(fmr(l,lo,up))