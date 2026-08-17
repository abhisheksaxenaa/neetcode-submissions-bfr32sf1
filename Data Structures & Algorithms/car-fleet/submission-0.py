'''
(7,1)(4,2)(1,2)(0,1)
'''
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        result = []
        max_heap = []
        stack = []
        prev_time = 0
        fleets = 0
        N = len(position)
        for i in range(N):
            heapq.heappush(max_heap, (-position[i], speed[i]))
        while max_heap:
            heap = heapq.heappop(max_heap)
            pos = heap[0] * -1
            sp = heap[1]
            time = (target - pos) / sp # 3 seconds
            if time > prev_time:
                fleets += 1
                prev_time = time
        return fleets
            
