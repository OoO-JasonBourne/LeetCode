class Solution:
    def splitNum(self, num: int) -> int:
        numArr = [int(_) for _ in str(num)]
        numArr.sort()
        num1 = int(''.join(map(str, numArr[0::2])))
        num2 = int(''.join(map(str, numArr[1::2])))
        return num1 + num2