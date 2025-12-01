class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        z = 0
        max_length = 0
        
        for right in range(len(nums)):
            
            # include nums[right]
            if nums[right] == 0:
                z += 1
            
            # shrink window if too many zeros
            while z > k:
                if nums[left] == 0:
                    z -= 1
                left += 1
            
            # window is valid here
            max_length = max(max_length, right - left + 1)
        
        return max_length
