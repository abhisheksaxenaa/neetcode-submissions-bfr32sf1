class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = [(0,0)] * (n + 1)
        for (i, j) in trust:
            (outi, ini) = people[i]
            (outj, inj) = people[j]
            people[i] = (outi + 1, ini)
            people[j] = (outj, inj + 1)

        for i in range(1, n + 1):
            (outdeg, indeg) = people[i]
            if outdeg == 0 and indeg == (n - 1):
                return i
        # print(people)
        return -1