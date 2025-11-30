class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # initial window sum
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        left = 0
        right = k
        
        # slide window
        while right < len(nums):
            window_sum = window_sum - nums[left] + nums[right]
            max_sum = max(max_sum, window_sum)
            
            left += 1
            right += 1
        
        return max_sum / k
