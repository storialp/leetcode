class Solution:
    def climbStairs(self, n: int, memo={}) -> int:
        if n in memo:
            return memo[n]
        elif n == 0 or n == 1:
            return 1
        else:
            memo[n] = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)
            return memo[n]