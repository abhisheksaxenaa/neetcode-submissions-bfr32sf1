# i from 0 to j = (i + nums[i])
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        i, j = 0, 0
        while i <= j and i < N and j < N:
            j = max(j, i + nums[i])
            i += 1
        return j >= N - 1