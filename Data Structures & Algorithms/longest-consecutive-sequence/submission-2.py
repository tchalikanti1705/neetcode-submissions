class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0

        for i in nums:
            if (i-1) not in hashset:
                length = 0
                while (i+length) in hashset:
                    length+=1
                longest = max(length, longest)
        return longest 
        