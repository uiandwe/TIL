package com.nts.algorithm;

import java.util.ArrayList;
import java.util.List;

class Solution46 {
	
	public void bt(int[] nums, List<List<Integer>> ret, List<Integer> temp){
		if(temp.size() == nums.length){
			ret.add(new ArrayList<Integer>(temp));
			return;
		}
		
		for(int num:nums){
			if(temp.contains(num)) continue;
			temp.add(num);
			bt(nums, ret, temp);
			temp.remove(temp.size()-1);
		}
	}
	
    public List<List<Integer>> permute(int[] nums) {
		List<List<Integer>> ret = new ArrayList<>();
		List<Integer> temp = new ArrayList<>();
		bt(nums, ret, temp);
		
        return ret;
    }
}


public class leetCode46 {

	public static void main(String[] args) {
		Solution46 s46 = new Solution46();
		int[] nums = {1, 2, 3};
		System.out.println(s46.permute(nums));
	}

}
