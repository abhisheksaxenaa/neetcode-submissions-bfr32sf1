class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, n in enumerate(nums):
            index = visited.get(target - n, -1)
            if index != -1:
                return [index, i]
            visited[n] = i
        return []