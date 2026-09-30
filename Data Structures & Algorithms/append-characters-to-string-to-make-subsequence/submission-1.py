class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sptr, tptr = 0, 0

        while sptr < len(s) and tptr < len(t):
            if s[sptr] == t[tptr]:
                sptr+=1
                tptr+=1
            elif s[sptr] != t[tptr]:
                sptr+=1
        return len(t) - tptr
        