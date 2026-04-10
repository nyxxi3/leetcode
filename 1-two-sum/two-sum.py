class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        #x+y = t => t-x = y
        for i,e in enumerate(nums):
            if target-e in hashmap:
                return [i,hashmap[target-e]]
            else:
                hashmap[e] = i
        