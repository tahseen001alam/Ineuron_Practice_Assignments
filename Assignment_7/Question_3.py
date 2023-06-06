def a_s(num1, num2):
    i, j = len(num1) - 1, len(num2) - 1
    ca = 0
    re = ""

    while i >= 0 or j >= 0:
        digit1 = int(num1[i]) if i >= 0 else 0
        digit2 = int(num2[j]) if j >= 0 else 0
        curr_sum = digit1 + digit2 + ca

        re += str(curr_sum % 10)
        ca = curr_sum // 10

        i -= 1
        j -= 1

    if ca > 0:
        re += str(carry)

    return re[::-1]
num1=input()
num2=input()
print(a_s(num1,num2))
