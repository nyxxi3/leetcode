//https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
class Solution {
    public int[] searchRange(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;
        int[] error = {-1, -1};

        while (start <= end) {
            int mid = start + (end - start) / 2;

            if (nums[mid] == target) {
                int foundIndex = mid;

                while (foundIndex < nums.length && nums[foundIndex] == target) {
                    foundIndex++;
                }
                int pos1 = foundIndex - 1;

                foundIndex = mid;
                while (foundIndex >= 0 && nums[foundIndex] == target) {
                    foundIndex--;
                }
                int pos2 = foundIndex + 1;

                int[] rangeArr = {pos2, pos1};
                return rangeArr;
            } else if (nums[mid] > target) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }

        return error;
    }
}
