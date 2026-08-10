class Solution:
    def reverseBits(self, n: int) -> int:
        # Need to check solution with divide and conquer
        result = 0
        for i in range(32):
            bit = (n >> i) & 1
            result += (bit << (31 - i))
        return result