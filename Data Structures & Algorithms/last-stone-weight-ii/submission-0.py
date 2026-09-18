'''
2,4,1,5,6,3

sort not required
1,2,3,4,5,6

-1+2+3-4-5+6
-(1+4+5) + (2+3+6) =

total = 21
sum part 1 = 11
sum part 2 = total - sum part 1
diff = abs(sum part 1 - sum part 2) = sum part 1 - (total - sum part 2) = 2 * sum part 1 - total


2,4,1,5,6,3

(3,0) -> (6,0)


'''
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        self.min_diff = float('inf')
        total = 0
        mem = {}
        for stone in stones:
            total += stone
        
        def solve(n, current):
            if n == 0:
                return current
            if f'{n}_{current}' in mem:
                return mem[f'{n}_{current}']
            no_choose = solve(n - 1, current)
            res = max(no_choose, solve(n - 1, current + stones[n - 1]))
            self.min_diff = min(self.min_diff, abs((2 * res) - total))
            mem[f'{n}_{current}'] = res
            return res

        solve(len(stones), 0)
        return self.min_diff
        