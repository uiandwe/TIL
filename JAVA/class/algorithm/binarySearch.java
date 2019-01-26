package com.nts.algorithm;

public class binarySearch {

	public static int binarySearch(int[] arr, int data){
		int left = 0;
		int right = arr.length-1;
		
		while(left <= right){
			int mid = (left+right)/2;
			if(arr[mid] == data){
				return mid;
			}
			else if (arr[mid] > data){
				right = mid-1;
			}
			else{
				left = mid+1;
			}
		}
		
		return -1;
	}
	
	public static void main(String[] args) {
		int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
		
		assert 5 == binarySearch(arr, 6);
		assert 0 == binarySearch(arr, 1);
	}

}
