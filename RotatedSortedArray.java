//https://leetcode.com/problems/search-in-rotated-sorted-array/description/
class Solution {
    public int search(int[] nums, int target) {
     int start = 0;
     int end = nums.length-1;   
      
     while(start<=end){
         int mid = start + (end-start)/2;
         if(nums[mid]==target){
             return mid;
         }
       //check if left part of the array is sorted
         if(nums[mid]>=nums[start]){
           //check if the target lies in the left part
             if(target>=nums[start] && target<=nums[mid]){
                 end = mid - 1;
             }
             else{
                 start = mid + 1;
             }
         }
       //right part of the array is sorted
         else{
           //check if target lies in the right part
             if (target>=nums[mid] && target<=nums[end]){
                 start = mid + 1;
             }
             else{
                 end = mid - 1;
             }
         }
     }
     return -1;
    }
}
