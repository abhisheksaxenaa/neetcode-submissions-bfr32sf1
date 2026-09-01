'''
18, 26, 20
'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        result = []
        N = len(points)
        i = 0
        while i < k:
            [x, y] = points[i]
            # print(x, y)
            distance = (x * x) + (y * y)
            # print(distance)
            heapq.heappush(max_heap, (-distance, x, y))
            i += 1
        # print(i)

        while i < N:
            (distance, x, y) = max_heap[0]
            [m, n] = points[i]
            new_distance = (m * m) + (n * n)
            if new_distance < -distance:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, (-new_distance, m, n))
            i += 1
        for (d, x, y) in max_heap:
            result.append([x,y])
        return result