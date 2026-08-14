class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        heapq.heapify(max_heap)
        N = len(nums)
        result = []

        for i in range(k - 1):
            heapq.heappush(max_heap, (nums[i] * -1, i)) # T(k.log(n))
        left = 0
        right = k - 1
        while right < N:
            heapq.heappush(max_heap, (nums[right] * -1, right))
            while max_heap and max_heap[0][1] < left:
                heapq.heappop(max_heap)
            result.append(max_heap[0][0] * -1)
            right += 1
            left += 1
        return result