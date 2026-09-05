class Solution:
    def checkArraySum(self, nums: List[int], currentSum: int, result: List[int], n: int):
        if currentSum == 0 and tuple(result) not in self.visited:
            self.final.append([*result])
            self.visited.add(tuple(result))
        if currentSum < 0 or n == 0:
            return
        self.checkArraySum(nums, currentSum, result, n - 1)
        if nums[n - 1] <= currentSum:
            result.append(nums[n - 1])
            self.checkArraySum(nums, currentSum - nums[n - 1], result, n)
            self.checkArraySum(nums, currentSum - nums[n - 1], result, n - 1)
            result.pop()

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.final = []
        self.visited = set()
        sorted(nums)
        self.checkArraySum(nums, target, [], len(nums))
        return self.final