class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        copy = []
        for n in nums:
            copy.append(n)
        for i,e in enumerate(copy):
            if e == 0:
                nums.remove(e)
                zero_count += 1
        while zero_count > 0:
            nums.append(0)
            zero_count -= 1
        
        