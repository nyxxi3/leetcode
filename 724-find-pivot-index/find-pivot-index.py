class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        
        for i in range(len(nums)):
            if i < len(nums):
                right_sum -= nums[i]
            if i-1 >= 0:
                left_sum += nums[i-1]
            if right_sum == left_sum:
                return i
        return -1

            
