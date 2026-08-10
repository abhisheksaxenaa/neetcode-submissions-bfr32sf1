class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            j = i
            count = 0
            while j > 0:
                count += (j & 1)
                j = j >> 1
            output.append(count)
        return output
        