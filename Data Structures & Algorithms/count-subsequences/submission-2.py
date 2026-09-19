class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M, N = len(s), len(t)
        # dp = [[-1] * (N + 1) for _ in range(M + 1)]
        # Top Down memoized approach
        # def solve(i, j):
        #     if j == 0:
        #         dp[i][j] = 1
        #         return 1
        #     if i == 0:
        #         dp[i][j] = 0
        #         return 0
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     temp = solve(i - 1, j)
        #     if s[i - 1] == t[j - 1]:
        #         temp += solve(i - 1, j - 1)
        #     dp[i][j] = temp
        #     return temp
        # total = solve(M, N)
        # return total

        # Bottom-Up approach
        # dp = [[0] * (N + 1) for _ in range(M + 1)]
        # for i in range(M + 1):
        #     dp[i][0] = 1
        # for i in range(1, M+1):
        #     for j in range(1, N + 1):
        #         dp[i][j] = dp[i-1][j]
        #         if s[i-1] == t[j-1]:
        #             dp[i][j] += dp[i-1][j-1]
        # return dp[M][N]
        dp = [0] * (N + 1)
        dp[0] = 1
        for i in range(1, M+1):
            curr = [0] * (N + 1)
            curr[0] = 1
            for j in range(1, N + 1):
                curr[j] = dp[j]
                if s[i-1] == t[j-1]:
                    curr[j] += dp[j-1]
            dp = curr
        return dp[N]