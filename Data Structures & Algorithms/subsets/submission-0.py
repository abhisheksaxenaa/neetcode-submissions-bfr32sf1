class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        P = int(math.pow(2, N))
        result = [[] for _ in range(P)]
        for i in range(1, P):
            pointer = 0
            j = i
            while j > 0:
                if j % 2 == 1:
                    result[i].append(nums[pointer])
                pointer += 1
                j = j >> 1
        return result