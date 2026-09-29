class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac, atl = set(), set()
        result = []
        
        def bfs(src, ocean):
            q = deque(src)
            while q:
                r, c = q.popleft()
                ocean.add((r, c))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < m and 0 <= nc < n and
                        (nr, nc) not in ocean and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        q.append((nr, nc))
        pacific = []
        atlantic = []
        for i in range(m):
            pacific.append((i, 0))
            atlantic.append((i, n - 1))

        for i in range(n):
            pacific.append((0, i))
            atlantic.append((m - 1, i))
        bfs(pacific, pac)
        bfs(atlantic, atl)
        # print(pac)
        # print(atl)

        for i in range(m):
            for j in range(n):
                if (i, j) in pac and (i, j) in atl:
                    result.append([i,j])
        return result