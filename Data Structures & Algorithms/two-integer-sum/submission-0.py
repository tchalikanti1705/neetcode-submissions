class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for idx, val in enumerate(nums):
            compl = target - val
            if compl in hmap:
                return [hmap[compl], idx]
            hmap[val] = idx
        return []
        