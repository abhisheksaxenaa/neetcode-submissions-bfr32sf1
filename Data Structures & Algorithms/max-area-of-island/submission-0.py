class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        R = len(grid)
        C = len(grid[0])
        # for each '1' cell change it to -1
        # calculate area by DFS
        def get_area(i, j, R, C):
            if i >= R or j >= C or i <0 or j < 0:
                return 0
            if grid[i][j] != 1:
                return 0
            grid[i][j] = -1
            la = get_area(i + 1, j, R, C)
            lb = get_area(i, j + 1, R, C)
            lc = get_area(i - 1, j, R, C)
            ld = get_area(i, j - 1, R, C)
            return la+lb+lc+ld+1

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    area = get_area(i, j, R, C)
                    max_area = max(max_area, area)
        return max_area