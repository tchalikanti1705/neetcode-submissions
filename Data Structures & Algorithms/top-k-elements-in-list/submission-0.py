class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}

        n = len(nums)
        for i in nums:
            hmap[i] = hmap.get(i, 0) + 1
        
        buckets = [[] for _ in range(n+1)]

        for value, count in hmap.items():
            buckets[count].append(value)

        res = []

        for i in range(len(buckets)-1, 0, -1):
            for val in buckets[i]:
                res.append(val)
                if len(res)==k:
                    return res
        

        