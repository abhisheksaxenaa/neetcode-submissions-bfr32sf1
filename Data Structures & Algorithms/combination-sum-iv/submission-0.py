class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        mem = {target: True}
        def solve(current):
            if current > target:
                return 0
            if current == target:
                return 1
            if current in mem:
                return mem[current]
            res = 0
            for i in range(len(nums)):
                if nums[i] + current <= target:
                    res += solve(current + nums[i])
            mem[current] = res
            return res
            # if choose or no_choose:
        return solve(0)
        