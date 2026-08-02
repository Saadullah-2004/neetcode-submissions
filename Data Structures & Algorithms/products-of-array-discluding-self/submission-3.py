class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        count = 1
        for i in range(len(nums)):
            prefix[i] = count
            count *= nums[i]
        
        count = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix[i] *= count
            count *= nums[i]

        return prefix


        