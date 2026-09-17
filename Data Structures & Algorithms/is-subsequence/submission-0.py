class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sptr, tptr = 0, 0

        count = 0

        while sptr<len(s) and tptr<len(t):
            if s[sptr] == t[tptr]:
                count+=1
                sptr+=1
                tptr+=1
            else:
                tptr+=1
        return count==len(s)
        