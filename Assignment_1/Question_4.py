def plusOne(digits):
    carry = 1  

    for i in range(len(digits) - 1, -1, -1):
        digit_sum = digits[i] + carry
        digits[i] = digit_sum % 10  
        carry = digit_sum // 10  
    if carry:
        digits.insert(0, carry) 

    return digits


digits = list(map(int,input().split()))
result = plusOne(digits)
print(result)
