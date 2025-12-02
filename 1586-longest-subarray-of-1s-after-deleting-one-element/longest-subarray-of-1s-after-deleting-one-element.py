class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        z = 0
        max_length = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                z += 1
            while z > 1:
                if nums[left] == 0:
                    z -=1
                left += 1
            length = right - left
            max_length = max(max_length, length)
        return max_length
