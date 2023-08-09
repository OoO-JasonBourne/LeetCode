class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        solve, mix = 1, 0
        for i in str(n):
            solve *= int(i)
            mix += int(i)
        return solve - mix