'''

'''
class Solution:
    def rec(self, i: int, j: int) -> int:
        # TC: O(2^(m + n))
        # TC: O(m + n)
        if i < 0 or j < 0:
            return 0
        if i == 0 and j == 0:
            return 1
        return self.rec(i - 1, j) + self.rec(i, j - 1)
    def uniquePaths(self, m: int, n: int) -> int:
        # return self.rec(m - 1, n - 1)
        # DP:
        # TC: O(m * n)
        # SC: O(m * n)
        # dp = [[0] * n for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 or j == 0:
        #             dp[i][j] = 1
        #         else:
        #             dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # return dp[m - 1][n - 1]
        # Space Optimized
        # row = [1] * n
        # for i in range(m - 1):
        #     newRow = [1] * n
        #     for j in range(1, n):
        #         newRow[j] = row[j] + newRow[j - 1]
        #     row = newRow
        # return row[n - 1]
        if m == 1 or n == 1:
            return 1
        if m < n:
            m, n = n, m

        res = j = 1
        for i in range(m, m + n - 1):
            res *= i
            res //= j
            j += 1

        return res