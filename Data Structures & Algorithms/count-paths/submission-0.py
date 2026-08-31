'''

'''
class Solution:
    def rec(self, i: int, j: int) -> int:
        if i < 0 or j < 0:
            return 0
        if i == 0 and j == 0:
            return 1
        return self.rec(i - 1, j) + self.rec(i, j - 1)
    def uniquePaths(self, m: int, n: int) -> int:
        # return self.rec(m - 1, n - 1, 0, 0)
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]