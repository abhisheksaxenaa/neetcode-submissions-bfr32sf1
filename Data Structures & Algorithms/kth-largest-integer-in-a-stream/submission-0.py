class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.size = k
        for num in nums:
            if len(self.min_heap) < k:
                heapq.heappush(self.min_heap, num)
            else:
                # check the top element
                # if num is greater then top element
                # then pop and push the num
                top = self.min_heap[0]
                if top < num:
                    heapq.heappop(self.min_heap)
                    heapq.heappush(self.min_heap, num)
        

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.size:
            heapq.heappush(self.min_heap, val)
        else:
            # check the top element
            # if num is greater then top element
            # then pop and push the num
            top = self.min_heap[0]
            if top < val:
                heapq.heappop(self.min_heap)
                heapq.heappush(self.min_heap, val)
        return self.min_heap[0]
