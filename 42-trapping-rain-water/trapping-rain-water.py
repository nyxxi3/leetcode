class Solution:
    def trap(self, height: List[int]) -> int:
        [4,2,0,3,2,5]
        #
        water_blocks = 0
        l = 0
        r = len(height)-1
        l_max,r_max = 0,0
        while l < r:
            l_max = max(l_max,height[l])
            r_max = max(r_max,height[r])
            if l_max < r_max:
                water_blocks += l_max - height[l]
                l += 1
            else:
                water_blocks += r_max - height[r]
                r -= 1

        return water_blocks
            


        