class Solution:
    def climbStairs(self, n: int) -> int:
        # def dfs(i):
        #     if i == n:
        #         return 1
        #     if i > n:
        #         return 0
        #     return dfs(i + 1) + dfs(i + 2)

        # return dfs(0)
        # DP Approach
        dp = [0] * (n + 2)
        dp[n] = 1
        dp[n + 1] = 0
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]
        return dp[0]