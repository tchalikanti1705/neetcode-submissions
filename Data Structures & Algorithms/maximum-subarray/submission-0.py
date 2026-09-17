class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursm = mxsm = nums[0]

        for i in range(1, len(nums)):
            cursm = max(cursm + nums[i], nums[i])
            mxsm = max(cursm, mxsm)
        return mxsm
        