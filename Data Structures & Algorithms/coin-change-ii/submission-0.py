class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        dp = [[0] * (amount + 1) for _ in range(N + 1)]

        for i in range(1, N + 1):
            for j in range(amount + 1):
                if j == 0:
                    dp[i][j] = 1
                elif coins[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
        return dp[N][amount]