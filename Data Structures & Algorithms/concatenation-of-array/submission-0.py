class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [0] * (2*len(nums))

        n = len(nums)

        for idx, value in enumerate(nums):
            res[idx] = value
            res[idx+n] = value
        
        return res
        