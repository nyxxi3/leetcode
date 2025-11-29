class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        s = float('inf')
        ss = float('inf')
        for n in nums:
            if n <= s:
                s = n
            elif n <= ss:
                ss = n
            else:
                return True
        return False