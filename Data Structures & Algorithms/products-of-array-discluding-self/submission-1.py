class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        suff = [1] * len(nums)
        for n in range(len(nums)):
            if n > 0:
                pre[n] = pre[n-1] * nums[n-1]
        for n in range(len(nums) - 1, -1, -1):
            if n < len(nums) - 1:
                suff[n] = suff[n+1] * nums[n+1]
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = pre[i] * suff[i]
        return res