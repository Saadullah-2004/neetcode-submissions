class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        min_length = float("inf")
        sum_arr = 0
        for end in range(len(nums)):
            sum_arr += nums[end]
            while sum_arr >= target:
                min_length = min(min_length, end - start + 1)
                sum_arr -= nums[start]
                start += 1
        return min_length if min_length != float("inf") else 0