class Solution:
    def alternateDigitSum(self, n: int) -> int:
        length = len(str(n))
        consult = n // (10 ** (length - 1))
        remainder = n % (10 ** (length - 1))
        posi = 1
        while remainder != 0:
            posi = -posi
            length -=1
            consult += remainder // (10 ** (length - 1)) * posi
            remainder = n % (10 ** (length - 1))
        consult += remainder
        return consult