class Solution:
    def get_max(self, nums: List[int], n) -> int:
        N = len(nums)
        if n >= N:
            return 0
        # TC: O(n^2)
        # SC: O(n)
        # Memoize verision
        # if money[n] != -1:
        #     return money[n]
        return max(nums[n] + self.get_max(nums, n + 2), self.get_max(nums, n + 1))

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # return self.get_max(nums, 0)
        money = [0] * (n+2)
        # TC: O(n)
        # SC: O(n)
        for i in range(n-1, -1, -1):
            money[i] = max(nums[i] + money[i + 2], money[i + 1])
        return max(money[0], money[1])
