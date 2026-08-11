class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        result = 0
        for num in nums:
            result = result ^ num
        for i in range(0, n):
            result = result ^ i
        return result
        # res = len(nums)

        # for i in range(len(nums)):
        #     res += i - nums[i]
        # return res