import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [(-val, idx) for idx, val in enumerate(gifts)]

        heapq.heapify(heap)

        while k:
            value, idx = heapq.heappop(heap)
            value = -value
            value = math.floor(math.sqrt(value))
            gifts[idx] = value
            heapq.heappush(heap, (-value, idx))
            k -= 1
        return sum(gifts)

        