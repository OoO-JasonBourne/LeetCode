def alternateDigitSum(n):
    # length = len(str(n))
    # consult = n // (10 ** (length - 1))
    # remainder = n % (10 ** (length - 1))
    # posi = 1
    # while remainder != 0:
    #     posi = -posi
    #     length -= 1
    #     consult += remainder // (10 ** (length - 1)) * posi
    #     remainder = n % (10 ** (length - 1))
    # consult += remainder
    # return consult
    res, sign = 0, 1
    while n:
        res += n % 10 * sign
        sign = -sign
        n //= 10
    return -sign * res


n = 521
print(alternateDigitSum(n))



