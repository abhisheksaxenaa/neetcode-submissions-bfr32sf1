'''
Check each direction and add:
    - 1 if it is on wall
    - 1 if it is the water
    - 0 if another land

'''
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0
        def isValidDirection(i: int, j: int) -> bool:
            return 0 <= i < R and 0 <= j < C

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    for (x,y) in d:
                        xi = i + x
                        yj = j + y
                        if not isValidDirection(xi, yj) or grid[xi][yj] != 1:
                            res += 1
        return res