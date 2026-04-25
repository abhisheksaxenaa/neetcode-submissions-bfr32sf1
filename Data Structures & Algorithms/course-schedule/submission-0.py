class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # make adjacency list of nodes
        # For each course that can be visited without cycle
        # mark them as possible
        # use topological sort?
        outdegree = [0] * numCourses
        courseTaken = 0
        adj = defaultdict(list)
        queue = deque()

        for course, pre in prerequisites:
            adj[pre].append(course)
            outdegree[course] += 1

        for i,course in enumerate(outdegree):
            if course == 0:
                queue.append(i)

        while queue:
            course = queue.popleft()
            courseTaken += 1
            for dep in adj[course]:
                outdegree[dep] -= 1
                if outdegree[dep] == 0:
                    queue.append(dep)

        return courseTaken == numCourses