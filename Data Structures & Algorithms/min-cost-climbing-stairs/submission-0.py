class Solution:
    # def ks(self, cost: List[int], n: int) -> int:
    #     if n >= len(cost):
    #         return 0
    #     return cost[n] + min(self.ks(cost, n + 1), self.ks(cost, n + 2))
    # [0,0,0,0,0]
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # return min(self.ks(cost, 0), self.ks(cost, 1))
        dp = [0] * (n + 2)
        for i in range(n - 1, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        # print(dp)
        return min(dp[0], dp[1])
