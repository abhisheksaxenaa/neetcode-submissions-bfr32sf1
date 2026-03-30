class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        visited = {}
        for i,n in enumerate(numbers):
            t = target - n
            f = visited.get(t, None)
            if f != None:
                return [f+1, i+1]
            if n not in visited:
                visited[n] = i
        return False
