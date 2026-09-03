'''
[1,2]
j = {0, 1}
i   result
0   []
1   [1]
2   [2]
3   [1,2]


pushing 1 bit to left side
j index is 0 or 1
With expr (1 << j)
either it will be
01 or 10

'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        P = int(math.pow(2, N))
        result = []
        result.append([])
        for i in range(1, P):
            subset = []
            for j in range(N):
                if i & (1 << j):
                    subset.append(nums[j])
            result.append(subset)
        return result