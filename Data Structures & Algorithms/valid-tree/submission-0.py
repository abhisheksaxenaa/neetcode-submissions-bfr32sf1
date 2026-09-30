class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        q = []
        for edge in edges:
            [u,v] = edge
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        q = deque([(0, -1)])
        visited.add(0)

        while q:
            node, parent = q.popleft()
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                visited.add(nei)
                q.append((nei, node))

        return len(visited) == n