class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        outdegree = [0] * numCourses
        courseTaken = []
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
            courseTaken.append(course)
            for dep in adj[course]:
                outdegree[dep] -= 1
                if outdegree[dep] == 0:
                    queue.append(dep)
        if len(courseTaken) != numCourses:
            return []
        return courseTaken