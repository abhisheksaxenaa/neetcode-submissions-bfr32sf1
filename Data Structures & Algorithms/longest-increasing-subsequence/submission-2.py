class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        mem = [[-1] * (n + 1) for _ in range(n + 1)]

        def solve(i: int, j: int):
            if i >= n or j >= n:
                return 0
            if mem[i][j] != -1:
                return mem[i][j]
            s = solve(i, j + 1)
            if i == -1 or nums[i] < nums[j]:
                s = max(s, solve(j, j + 1) + 1)
            mem[i][j] = s
            return s
        return solve(-1, 0)