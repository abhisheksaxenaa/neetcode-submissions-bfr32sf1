class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1
        while l < h:
            mid = l + ((h - l) // 2)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        return l + 1 if nums[l] < target else l