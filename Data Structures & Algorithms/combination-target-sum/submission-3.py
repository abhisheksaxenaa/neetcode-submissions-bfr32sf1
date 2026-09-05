class Solution:
    def checkArraySum(self, nums: List[int], currentSum: int, target: int, result: List[int], n: int):
        if currentSum == target:
            self.final.append([*result])
            return
        if currentSum > target or n >= len(nums):
            return
        result.append(nums[n])
        self.checkArraySum(nums, currentSum + nums[n], target, result, n)
        result.pop()
        self.checkArraySum(nums, currentSum, target, result, n + 1)

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.final = []
        self.visited = set()
        sorted(nums)
        self.checkArraySum(nums, 0, target, [], 0)
        return self.final