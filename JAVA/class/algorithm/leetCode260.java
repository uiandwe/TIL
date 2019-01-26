package com.nts.algorithm;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;

public class leetCode260 {

	public int[] singleNumber(int[] nums) {
		HashSet<Integer> hs = new HashSet<>();
        for(int number: nums){
            if(hs.contains(number)){
            	hs.remove(number);
            }
            else{
            	hs.add(number);
            }
        }
        
        Iterator<Integer> it = hs.iterator();
        int[] ret = new int[hs.size()];
        int i = 0;
        while(it.hasNext()){
        	ret[i] = it.next();
        	i++;
        }
        
        return ret;
    }
    
	public static void main(String[] args) {
		leetCode260 lc = new leetCode260();
		int[] nums = {1,2,1,3,2,5};
		for(int number : lc.singleNumber(nums)){
			System.out.println(number);
		}

	}

}
