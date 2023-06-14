class Solution {
    public int findMin(int[] nums) {
        int start = 0;
        int end = nums.length-1;
        int min = Integer.MAX_VALUE;
        while(start<=end){
            int mid = start + (end-start)/2;
            if(nums[mid]>=nums[start]){
                //left part is sorted
                if(min>nums[start]){
                min = nums[start];
                }
                start = mid + 1;
            }
            else{
                //right part is sorted
                if(min>nums[mid]){
                min = nums[mid];
                }
                end = mid - 1;
            }
        }
        return min;
    }
}
