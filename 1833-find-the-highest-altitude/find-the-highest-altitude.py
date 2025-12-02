class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        mc = 0
        for i in range(len(gain)):
            current = current + gain[i]
            mc = max(current,mc)
        return mc
