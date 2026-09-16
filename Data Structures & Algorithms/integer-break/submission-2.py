class Solution:
    def solve(self, num: int, n: int):
        if num == 1:
            return 1
        if self.dp[num] != -1:
            return self.dp[num]
        res = 0 if num == n else num
        for i in range(1, num):
            val = self.solve(i, n) * self.solve(num - i, n)
            res = max(res, val)
        self.dp[num] = res
        return res

    def integerBreak(self, n: int) -> int:
        self.dp = [-1] * (n + 1)
        self.solve(n, n)
        return self.dp[n]