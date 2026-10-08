class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        n = len(nums)
        while j < n:
            if nums[i] != nums[j]:
                nums[i + 1] = nums[j]
                i += 1
            j += 1
        return i + 1