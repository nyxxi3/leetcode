class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        return max(freq, key=freq.get)
