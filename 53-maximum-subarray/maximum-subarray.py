class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = float('-inf')
        for current_num in nums:
            current_sum = max(current_num,current_num+current_sum)
            max_sum = max(max_sum,current_sum)
        return max_sum