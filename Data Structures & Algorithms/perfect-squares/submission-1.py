'''

solve(0)->solve(1)->solve(2)->solve(3)->solve(4)
'''
class Solution:
    def numSquares(self, n: int) -> int:
        N = math.ceil(math.sqrt(n))
        # mem = {0: 0}

        # def solve(current):
        #     if current in mem:
        #         return mem[current]
        #     res = current
        #     for i in range(1, N + 1):
        #         if (i * i) > current:
        #             break
        #         res = min(res, 1 + solve(current - (i * i)))
        #     mem[current] = res
        #     return res
        # return solve(n)
        mem = [0] * (n + 1)
        mem[1] = 1
        for i in range(2, n + 1):
            res = i
            for j in range(1, N + 1):
                if (j * j) > i:
                    break
                res = min(res, 1 + mem[i - (j * j)])
            mem[i] = res
        return mem[n]