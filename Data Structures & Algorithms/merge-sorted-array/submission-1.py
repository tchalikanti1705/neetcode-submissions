class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0

        for idx, val in enumerate(nums1):
            if val == 0 and i < n:
                nums1[idx] = nums2[i]
                i += 1
        nums1.sort()


        
        