class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result = [[],[]]
        nums = set(nums1 + nums2)
        for i in nums:
            if i not in nums2:
                result[0].append(i)
            if i not in nums1:
                result[1].append(i)
        return result

        