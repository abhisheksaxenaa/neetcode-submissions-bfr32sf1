class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        total = 0
        for n in nums:
            total = total ^ n
        return total