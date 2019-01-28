package com.nts.algorithm;


class QuickSort1{
	
	public void sort(int[] nums, int left, int right) {
		if(nums.length<=1) {
			return ;
		}
		
		int i, j, temp, pivot;
		i = left;
		j = right;
		
		while(i<j) {
			pivot = nums[(left+right)/2];
			while(pivot < nums[j]) j--;
			while(i<j && nums[i] < pivot) i++;
			
			temp = nums[i];
			nums[i] = nums[j];
			nums[j] = temp;
			
			sort(nums, left, i-1);
			sort(nums, i+1, right);
		}
		
	}
	
}

public class testDemo {

	public static void main(String[] args) {
		QuickSort1 q = new QuickSort1();
		int[] nums = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
		q.sort(nums, 0, nums.length-1);
		for(int num:nums) {
			System.out.print(num+"\t");
		}
		
		

	}

}
