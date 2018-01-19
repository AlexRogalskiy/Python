def PowerDigitSum(value):
    sumDigit = 0
    while value > 0:
        mod = value % 10
        value = value / 10
        sumDigit = sumDigit + mod
    return sumDigit
        
print PowerDigitSum(2**1000)