class Solution:
    def maxDifference(self, s: str) -> int:
        frq = {}

        for c in s:
            frq[c] = frq.get(c, 0) + 1

        odd = []
        even = []

        for freq in frq.values():
            if freq % 2 == 1:
                odd.append(freq)
            else:
                even.append(freq)

        return max(odd) - min(even)
