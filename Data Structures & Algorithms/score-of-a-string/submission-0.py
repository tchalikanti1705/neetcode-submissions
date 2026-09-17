class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        left, right = 0, 1
        while right<len(s):
            res += abs( (ord(s[left])-ord('a')) - (ord(s[right]) - ord('a')) )
            left+=1
            right+=1
        return res
        