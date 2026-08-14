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
            # Get top element which is in the window

            (top, i) = heapq.heappop(max_heap)
            while max_heap and (right < i or i < left):
                (top, i) = heapq.heappop(max_heap)
            top = top * -1
            result.append(top)
            heapq.heappush(max_heap, (top * -1, i))
            # while max_heap:
            #     element = heapq.heappop(max_heap) * -1
            #     if element == nums[left]:
            #         break
            #     removed_elements.append(element)
            # for element in removed_elements:
            #     heapq.heappush(max_heap, element * -1)
            # max_heap.remove(nums[left] * -1)
            # heapq.heapify(max_heap)
            # print(nums[right], max_heap)
            right += 1
            left += 1
        return result