class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1)<0 or len(word2)<0:
            return ""
        res = ""
        w1ptr, w2ptr = 0, 0
        w1 = True if len(word1) > len(word2) else False
        while w1ptr < len(word1) and w2ptr < len(word2):
            res+=word1[w1ptr]
            res+=word2[w2ptr]
            w1ptr+=1
            w2ptr+=1
        if w1:
            while w1ptr < len(word1):
                res+=word1[w1ptr]
                w1ptr+=1
        else:
            while w2ptr < len(word2):
                res+=word2[w2ptr]
                w2ptr+=1
        return res
        