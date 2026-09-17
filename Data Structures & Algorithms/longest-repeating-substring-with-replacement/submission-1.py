class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = {}
        res = 0
        left = 0

        for right in range(len(s)):
            hmap[s[right]] = hmap.get(s[right], 0) + 1

            while ((right - left + 1) - max(hmap.values())) > k:
                hmap[s[left]]-=1
                left+=1
            
            res = max(res, right - left + 1)
        return res
        