

def fEN(n):
    n1 = len(n)
    num_set = set()
    duplicate = -1
    missing = -1

    for num in n:
        if num in num_set:
            duplicate = num
        num_set.add(num)

    for i in range(1, n1 + 1):
        if i not in num_set:
            missing = i
            break

    return [duplicate, missing]

n = list(map(int,input().split()))
result = fEN(n)
print(result)
