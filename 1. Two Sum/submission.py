class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_idx = dict()

        for idx in range(len(nums)):
            num_idx[nums[idx]] = idx
        
        for idx in range(len(nums)):
            t_num = target - nums[idx]
            if t_num in num_idx and idx != num_idx[t_num]:
                return [idx, num_idx[t_num]]
        return []
