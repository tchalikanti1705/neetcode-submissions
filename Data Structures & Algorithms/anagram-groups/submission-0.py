from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)

        for eachstr in strs:
            count = [0] * 26

            for eachchar in eachstr:
                count[ord(eachchar) - ord("a")] += 1
            
            hmap[tuple(count)].append(eachstr)
        
        return list(hmap.values())

        