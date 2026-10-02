import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            largest1 = -heapq.heappop(heap)
            largest2 = -heapq.heappop(heap)

            if largest1 != largest2:
                heapq.heappush(heap, -(largest1 - largest2))

        return -heap[0] if heap else 0
