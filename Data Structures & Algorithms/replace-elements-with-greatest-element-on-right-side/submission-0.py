class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        rightmx = -1

        for i in range(len(arr)-1, -1, -1):
            res[i] = rightmx
            rightmx = max(rightmx, arr[i])
        return res

        