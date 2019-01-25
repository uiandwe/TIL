package com.nts.algorithm;


public class QuickSort {
	
	public void quickSort(int[] arr, int left, int right){
		int i, j, temp, pivot;
		i = left;
		j = right;
		while(i < j){
			pivot = arr[(left+right)/2];
			while(pivot < arr[j]) j--;
			while(i < j && arr[i] <= pivot) i++;
			
			temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
			
			quickSort(arr, left, i - 1);
			quickSort(arr, i + 1, right);
					
		}
	}
	
	public static void main(String[] args) {
		QuickSort qs = new QuickSort();
		int[] arr = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
		qs.quickSort(arr, 0, arr.length-1);
		
		for(int i : arr){
			System.out.println(i);
		}

	}

}
