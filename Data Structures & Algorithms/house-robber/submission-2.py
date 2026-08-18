class Solution:
    def get_max(self, nums: List[int], n) -> int:
        if n <= 0:
            return 0
        return max(nums[n - 1] + self.get_max(nums, n - 2), self.get_max(nums, n - 1))

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # return self.get_max(nums, n)
        money = [0] * (n+2)
        for i in range(n-1, -1, -1):
            money[i] = max(nums[i] + money[i + 2], money[i + 1])
        return max(money[0], money[1])
