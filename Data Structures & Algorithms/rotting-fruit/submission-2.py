class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        t = 0
        q = deque()
        R = len(grid)
        C = len(grid[0])
        F = 0
        D = [(1, 0), (0, 1), (-1, 0), (0, -1)] # directions: down, right, up, left
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    F += 1
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
                    if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 1:
                        F -= 1
                        grid[nx][ny] = 2
                        q.append((nx, ny))
            if q:
                t += 1
        if F != 0:
            return -1
        return t
