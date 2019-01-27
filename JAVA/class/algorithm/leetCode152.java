package com.nts.algorithm;


class Solution152 {
    public int maxProduct(int[] nums) {
    	if(nums.length <= 0) return 0;
        int[][] d = new int[2][nums.length];
        d[0][0] = nums[0];
        d[1][0] = nums[0];

        for(int i=1; i<nums.length; i++){
        	d[0][i] = Math.max(nums[i], Math.max(d[0][i-1]*nums[i], d[1][i-1]*nums[i]));
        	d[1][i] = Math.min(nums[i], Math.min(d[0][i-1]*nums[i], d[1][i-1]*nums[i]));
        }
        
        int ret_max = Integer.MIN_VALUE;
        for(int i=0; i<nums.length; i++){
        	ret_max = Math.max(ret_max, Math.max(d[0][i], d[1][i]));
        }
        return ret_max;
    }
}


public class leetCode152 {

	public static void main(String[] args) {
		Solution152 s = new Solution152();
		int[] nums = {2, 3, -2, 4};
		assert 6 == s.maxProduct(nums);
		
		int[] nums1 = {-2, 0, -1};
		assert 0 == s.maxProduct(nums1);
		
		int[] nums2 = {2, 3, -2, 4, -1};
		assert 48 == s.maxProduct(nums2);
		
		int[] nums3 = {0, 2};
		assert 2 == s.maxProduct(nums3);

	}

}
