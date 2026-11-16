class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        target_arr = [0] * len(nums)
        for i in range(len(nums)):
            nums_dict[nums[i]] = i
            target_arr[i] = target - nums[i]
        for i in range(len(target_arr)):
            if target_arr[i] in nums_dict and nums_dict[target_arr[i]] != i:
                return sorted([i, nums_dict[target_arr[i]]])