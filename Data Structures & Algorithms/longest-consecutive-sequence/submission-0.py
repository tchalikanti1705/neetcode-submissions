class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)

        longest = 0

        for i in nums:
            length = 0
            if (i-1) not in hashSet:
                while i+length in hashSet:
                    length+=1
                longest = max(longest, length)
        return longest 