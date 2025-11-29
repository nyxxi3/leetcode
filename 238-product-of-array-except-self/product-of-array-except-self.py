class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #take 3 arrays
        # one for storing prefix product, another for suffix product, one for result
        #run two loops - one for prefix product (nums before an element i, excluding itself)
        # one for suffix product (nums after an element i excluding itself)
        #multiply respective elements in both array and return
        n = len(nums)
        res = [1]*n
        pref = 1 #starts with nothing
        for i in range(n):
            res[i] = pref
            pref *= nums[i]
        suf = 1
        for i in range(n-1,-1,-1):
            res[i] *= suf
            suf *= nums[i]
        return res



