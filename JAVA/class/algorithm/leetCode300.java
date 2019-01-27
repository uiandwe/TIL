package com.nts.algorithm;


class Solution300 {
    public int lengthOfLIS(int[] nums) {
    	if(nums.length == 0) return 0;
        int[] d = new int[nums.length];
        d[0] = 1;
        
        for(int i=1; i<d.length; i++){
        	int max = 0;
        	for(int j=0; j<i; j++){
        		if(nums[i] > nums[j] && max < d[j]){
        			max = d[j];
        		}
        	}
        	d[i] = max+1;
        }
        
        
        int ret_max = 0;
        for(int num: d){
        	ret_max = Math.max(ret_max, num);
        }
        return ret_max;
        
    }
}


public class leetCode300 {

	public static void main(String[] args) {
		Solution300 s300 = new Solution300();
		int[] nums = {10,9,2,5,3,7,101,18};
		System.out.println(s300.lengthOfLIS(nums));

		
		int[] nums1 = {10,9,2,5,3,7,101,18, 200};
		System.out.println(s300.lengthOfLIS(nums1));
		
		int[] nums2 = {10,9,8, 7, 6, 5, 4, 3, 2};
		System.out.println(s300.lengthOfLIS(nums2));
		
	}

}
