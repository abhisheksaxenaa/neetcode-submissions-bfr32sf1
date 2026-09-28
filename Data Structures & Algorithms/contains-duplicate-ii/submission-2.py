class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k < 1:
            return False
        window = {}
        i = 0
        j = 0
        n = len(nums)
        while j <= k and j < n:
            if nums[j] in window:
                return True
            window[nums[j]] = j
            j += 1
        while j < n:
            # print(f'{i} : {j}')
            del window[nums[i]]
            if nums[j] in window:
                return True
            window[nums[j]] = j
            i += 1
            j += 1
        return False