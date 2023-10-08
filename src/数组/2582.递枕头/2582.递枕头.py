class Solution:
    def passThePillow(self, n: int, time: int) -> int:
      arr = list(range(1, n+1)) + list(range(n-1, 0, -1))
      return arr[time % (2*(n - 1))]