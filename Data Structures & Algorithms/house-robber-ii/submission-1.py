class Solution:
    def rob_house(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        money = [0] * (n + 2)
        for i in range(n - 1, -1, -1):
            money[i] = max(nums[i] + money[i + 2], money[i + 1])
        return max(money[0], money[1])

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_money = max(self.rob_house(nums[1:]), self.rob_house(nums[:-1]))
        return max_money
        