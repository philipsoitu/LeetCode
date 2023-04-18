class Solution:
    def twoSum(self, nums, target: int):
        hm = {}
        for i in range(len(nums)):
            
            if nums[i] in hm:
                return [hm[nums[i]], i]
            else:
                a = target - nums[i]
                hm[a] = i

