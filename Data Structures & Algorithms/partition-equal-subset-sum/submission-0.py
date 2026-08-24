'''
S1 = sum(i)
S2 = sum(j)

S1 + S2 = sum(i) + sum(j) = sum(nums)

S1 = sum(nums) // 2

1. If even sum then only can divide
2. Check if the S1 can be made with given nums
    - if sum == 0, then return true
    - if i < 0, then return False
    - take choice as:
        - if number <= sum, choose the number
        - don't choose the number
'''
class Solution:
    def caluculate_sum(self, nums: List[int], i: int, total: int) -> bool:
        if total == 0:
            return True
        if i >= len(nums):
            return False
        if nums[i] > total:
            return self.caluculate_sum(nums, i + 1, total)
        return self.caluculate_sum(nums, i + 1, total - nums[i]) or self.caluculate_sum(nums, i + 1, total)

    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return True
        total = 0
        for n in nums:
            total += n
        if total % 2 != 0:
            return False
        total = total // 2
        return self.caluculate_sum(nums, 0, total)
        # n = len(nums)
        # calculate_sum = [[False] * (total + 1)] * (n + 1)
        # for i in range(n + 1):
        #     for j in range(total + 1):
        #         if j == 0:
        #             calculate_sum[i][j] = True
        #         if i == 0:
        #             calculate_sum[i][j] = False
        #         if nums[i - 1] > j:
        #             calculate_sum[i][j] = calculate_sum[i - 1][j]
        #         else:
        #             calculate_sum[i][j] = calculate_sum[i - 1][j] or calculate_sum[i - 1][j - nums[i - 1]]
        # return calculate_sum[n][total]
