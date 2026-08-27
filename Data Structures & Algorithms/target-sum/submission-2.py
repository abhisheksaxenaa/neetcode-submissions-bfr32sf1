class Solution:
    def find_choices(self, nums: List[int], n: int, current: int, target: int) -> int:
        # TC: O(2 ^ n) -> if recursion only
        # TC: O(n * m) -> if recurison + cached. n -> length of nums, m is 𝚺(nums)i
        if n == 0:
            return 1 if current == target else 0
        if (n, current) in self.dp:
            return self.dp[(n, current)]
        self.dp[(n, current)] = self.find_choices(nums, n - 1, current + nums[n - 1], target) + self.find_choices(nums, n - 1, current - nums[n - 1], target)
        return self.dp[(n, current)]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        self.dp = {}
        return self.find_choices(nums, n, 0, target)
        # if n == 0:
        #     return 1

        # total = 0
        # for num in nums:
        #     total += num
        # checksum = ((target + total) // 2)

        # dp = [[False] * (checksum + 1) for _ in range(n + 1)]
        # for i in range(n + 1):
        #     for j in range(checksum + 1):
        #         if j == 0:
        #             dp[i][j] = True
        #         elif i == 0:
        #             dp[i][j] = False
        #         elif nums[i - 1] > j:
        #             dp[i][j] = dp[i - 1][j]
        #         else:
        #             dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
        #         # dp[i][j] = left + right
        # total = 0
        # print(dp)
        # for i in range(checksum + 1):
        #     total += 1 if dp[n][i] else 0
        # return total