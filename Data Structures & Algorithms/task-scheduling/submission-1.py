'''
"A","A","A","A","A","A","B","C","D","E","F","G"

A->B->A->C->A->D->A->E->A->F->A->G
'''
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_count = [0] * 26
        max_count = 0
        maxF = 0
        time = 0
        for t in tasks:
            index = ord(t) - ord('A')
            tasks_count[index] += 1
            max_count = max(max_count, tasks_count[index])
        for i in tasks_count:
            maxF += 1 if i == max_count else 0

        time = (max_count - 1) * (n + 1) + maxF
        return max(len(tasks), time)