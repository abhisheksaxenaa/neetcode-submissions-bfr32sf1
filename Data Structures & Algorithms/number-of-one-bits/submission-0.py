class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        # print(n)
        while n > 0:
            ones += (n & 1)
            n = n >> 1
        return ones