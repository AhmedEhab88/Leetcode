def alternateDigitSum(n: int) -> int:
    sum = 0
    if len(str(n)) % 2 == 0:
        sign = True
    else:
        sign = False

    while n > 0:
        digit = n % 10
        if sign is False:
            sum += digit
        elif sign is True:
            sum -= digit
        n = n // 10
        sign = not sign
    return sum


print(alternateDigitSum(10))
