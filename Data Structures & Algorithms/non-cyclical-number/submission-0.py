class Solution:
    def splitNumber(self, n: int):
        return list(map(int, list(str(n))))
    def getSum(self, n: int) -> int:
        isValid = True
        visited = set()
        while n != 1:
            arr = self.splitNumber(n)
            total = 0
            for i in arr:
                total += (i * i)
            if total in visited:
                return total
            else:
                visited.add(total)
                n = total
        return n
        
    def isHappy(self, n: int) -> bool:
        result = self.getSum(n)
        return result == 1