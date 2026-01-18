class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       #create a hashmap
     #loop
      # at each iteration calculate target - x
      # check if target - x exists in the hashmap
      #if yes, return the current index and the found value's index
      # else, add the current val, index to the hashmap and move to next number
      hashmap = {}
      for i,e in enumerate(nums):
        if target - e in hashmap:
            return [i,hashmap[target-e]]
        else:
            hashmap[e] = i
        