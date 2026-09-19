class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = {}

        for i in nums:
            hmap[i] = hmap.get(i, 0) + 1
        
        for k, v in hmap.items():
            if v>len(nums)//2:
                return k      