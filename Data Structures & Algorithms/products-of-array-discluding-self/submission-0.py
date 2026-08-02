class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        count = 1
        for i in range(len(nums)):
            count *= nums[i]
            prefix[i] = count
        
        count = 1
        for i in range(len(nums) - 1, -1, -1):
            count *= nums[i]
            postfix[i] = count

        output = [0] * len(nums)

        for i in range(len(nums)):
            product = 1
            pre = i - 1
            post = i + 1
            if pre > -1:
                product *= prefix[pre]
            if post < len(nums):
                product *= postfix[post]
            output[i] = product
        return output
        print(prefix)
        print(postfix)


        