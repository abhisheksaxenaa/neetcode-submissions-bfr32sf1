class Solution:
    def checkArraySum(self, nums: List[int], currentSum: int, target: int, result: List[int], n: int):
        # print(currentSum, result, n)
        if currentSum == target:
            # print(result)
            self.final.append([*result])
            return
        for i in range(n, len(nums)):
            if i > n and nums[i] == nums[i - 1]:
                continue
            if currentSum + nums[i] > target:
                break
            result.append(nums[i])
            self.checkArraySum(nums, currentSum + nums[i], target, result, i + 1)
            result.pop()
            # if cu
        # result.append(nums[n])
        # while n + 1 < len(nums) and nums[n] == nums[n + 1]:
        #     n += 1
        # self.checkArraySum(nums, currentSum, target, result, n + 1)

    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        self.final = []
        nums.sort()
        # N = len(nums)
        # for i in range()
        self.checkArraySum(nums, 0, target, [], 0)
        return self.final
        # res = []
        # candidates.sort()

        # def dfs(idx, path, cur):
        #     if cur == target:
        #         res.append(path.copy())
        #         return
        #     for i in range(idx, len(nums)):
        #         if i > idx and nums[i] == nums[i - 1]:
        #             continue
        #         if cur + nums[i] > target:
        #             break

        #         path.append(nums[i])
        #         dfs(i + 1, path, cur + nums[i])
        #         path.pop()

        # dfs(0, [], 0)
        # return res