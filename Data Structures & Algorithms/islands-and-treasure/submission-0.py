class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        R = len(grid)
        C = len(grid[0])
        D = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    q.append((i,j))
        # visit each cell and traverse adjacent and assign the nearest part
        # bfs here
        while q:
            size = len(q)
            c = 0
            while c < size:
                (x, y) = q.popleft()
                c += 1
                val = grid[x][y]
                for i,j in D:
                    nx = x + i
                    ny = y + j
                    if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] > (grid[x][y] + 1):
                        grid[nx][ny] = grid[x][y] + 1
                        q.append((nx, ny))

