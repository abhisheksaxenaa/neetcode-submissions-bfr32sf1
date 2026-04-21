class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R = len(grid)
        C = len(grid[0])
        count = 0
        # Maintain count with 1, counting number of islands
        # Iterate through each cell
        # once '1' is found, change all connected 1s to -1 (a constant value to keep track of visited)
        # finding connected 1s via dfs?
        # return (count - 1)
        def dfs(i, j, R, C):
            if i >= R or j >= C or i < 0 or j < 0:
                return
            if grid[i][j] != '1':
                return
            grid[i][j] = '-1'
            dfs(i + 1, j, R, C)
            dfs(i, j + 1, R, C)
            dfs(i - 1, j, R, C)
            dfs(i, j - 1, R, C)

        for i in range(R):
            for j in range(C):
                if grid[i][j] == '1':
                    # print(f'{i}-{j}')
                    # put dfs
                    count += 1
                    dfs(i, j, R, C)
        # print(grid)
        return count
