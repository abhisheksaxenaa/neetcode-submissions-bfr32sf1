class Solution:
    def solve(self, piles: List[int], i: int, j: int):
        key = f'{i}_{j}'
        # if total <0:
            # self.mem[key] = True
            # return True
        if i > j:
            self.mem[key] = 0
            return 0
        if key in self.mem:
            return self.mem[key]
        # let's take from front
        alice_turn = (j - i) % 2 == 0
        front = piles[i] if alice_turn else 0
        rear = piles[j] if alice_turn else 0
        frontPick = self.solve(piles, i + 1, j) + front
        rearPick = self.solve(piles, i, j - 1) + rear
        self.mem[key] = max(frontPick, rearPick)
        return max(frontPick, rearPick)
    
    def stoneGame(self, piles: List[int]) -> bool:
        total = 0
        self.mem = {}
        for pile in piles:
            total += pile
        alice = self.solve(piles, 0, len(piles) - 1)
        return alice > total - alice