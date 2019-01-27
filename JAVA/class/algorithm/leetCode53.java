package com.nts.algorithm;

class Solution53 {
    public int maxSubArray(int[] nums) {
    	
        int[] d = new int[nums.length];
        d[0] = nums[0];
        
        for(int i=1; i<nums.length; i++){
        	d[i] = Math.max(d[i-1]+nums[i], nums[i]);
        }
        
        int ret_max = Integer.MIN_VALUE;
        for(int num: d){
        	ret_max = Math.max(ret_max, num);
        }
        return ret_max;
    }
}


public class leetCode53 {

	public static void main(String[] args) {
		Solution53 s = new Solution53();
		int[] nums = {-2,1,-3,4,-1,2,1,-5,4};
		assert 6 == s.maxSubArray(nums);

	}

}
