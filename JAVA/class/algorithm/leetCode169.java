package com.nts.algorithm;

import java.util.HashMap;


class Solution {
	HashMap<Integer, Integer> hm = new HashMap<>();
    public int majorityElement(int[] nums) {
    	int ret_max_index = 0;
    	int ret_max_val = 0;
        for(int number: nums){
        	if(hm.containsKey(number)){
        		hm.put(number, hm.get(number)+1);
        	}
        	else{
        		hm.put(number, 1);
        	}
        }
        
        for(int key : hm.keySet()){
        	if(hm.get(key) >  ret_max_val){
        		ret_max_index = key;
        		ret_max_val = hm.get(key);
        	}
        }
        
        return ret_max_index;
    }
}

public class leetCode169 {
	
	public static void main(String[] args) {
		Solution s = new Solution();
		int[] nums = {3,3,4};
		assert 3 == s.majorityElement(nums);

	}

}
