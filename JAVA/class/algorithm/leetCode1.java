package com.nts.algorithm;

import java.util.Arrays;
import java.util.HashMap;

public class leetCode1 {

	public int[] soluction(int[] nums, int target){
		HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();
		for(int i=0; i<nums.length; i++){
			int cur = nums[i];
			if(hm.containsKey(target-cur)){
				int[] ret = new int[2];
				ret[0] = hm.get(target-cur);
				ret[1] = i;
				return ret;
			}
			else{
				hm.put(cur, i);
			}
		}
		return nums;
	}
	
	public static void main(String[] args) {
		leetCode1 lc = new leetCode1();
		int[] arr = {2, 7, 11, 15};
		int[] assert_data = {0, 1};
		assert Arrays.equals(assert_data, lc.soluction(arr, 9));
		
	}

}
