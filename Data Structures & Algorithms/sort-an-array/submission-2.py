class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def counting_sort(nums):
            hmap = {}
            minval, maxval = min(nums), max(nums)
            for i in nums:
                hmap[i] = hmap.get(i, 0) + 1
            
            idx = 0
            for val in range(minval, maxval+1):
                if val in hmap:
                    while hmap[val] > 0 :
                        nums[idx] = val
                        idx += 1
                        hmap[val] -= 1

        counting_sort(nums)
        return nums
        