import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        heap = [(val, idx) for idx, val in enumerate(nums)]

        heapq.heapify(heap)

        while k:
            value, idx = heapq.heappop(heap)
            value *= multiplier
            nums[idx] = value
            heapq.heappush(heap, (value, idx))
            k -= 1
        return nums
        