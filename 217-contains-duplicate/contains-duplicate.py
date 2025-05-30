class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for i in nums:
            if i in hash and hash[i] == 1:
                return True
            elif i in hash:
                hash[i] += 1
            else:
                hash[i] = 1
        return False