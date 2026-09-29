class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sets = set(nums)
        longest = 0

        for n in nums:
            if n-1 not in sets:
                length = 0
                while (n + length) in sets:
                    length+=1
                longest = max(longest, length)
        return longest 

        