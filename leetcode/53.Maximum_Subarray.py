# Given an integer array nums, find the subarray with the largest sum, and return its sum.
# medium 
# accepted code

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        current_sum = nums[0]
        best_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(current_sum + num, num)
            if current_sum > best_sum:
                best_sum = current_sum
        return best_sum