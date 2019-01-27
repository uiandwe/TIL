package com.nts.algorithm;

import java.util.Collections;
import java.util.PriorityQueue;

class Solution215 {
	PriorityQueue<Integer> pq = new PriorityQueue<>();
    public int findKthLargest(int[] nums, int k) {
    	for(int num: nums){
    		if(pq.size() < k){
    			pq.offer(num);
    		}
    		else{
    			if(pq.peek() < num){
    				pq.poll();
    				pq.offer(num);
    			}
    		}
    	}
    	
        return pq.peek();
    }
}


public class leetCode215 {

	public static void main(String[] args) {
		Solution215 s215 = new Solution215();
		int[] nums = {3, 2, 1, 5, 6, 4};
		System.out.println(s215.findKthLargest(nums, 2));

	}

}
