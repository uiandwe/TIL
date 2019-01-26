package com.nts.algorithm;

import java.util.HashSet;
import java.util.Iterator;

public class leetCode136 {

	public int soluction1(int[] arr){
		int d = 0;
		for(int number : arr){
			d ^= number;
		}
		return d;
	}
	
	public int soluction(int[] arr){
		HashSet<Integer> hs = new HashSet<Integer>();
		for(int number : arr){
			if(hs.contains(number)){
				hs.remove(number);
			}
			else{
				hs.add(number);
			}
		}
		
		Iterator<Integer> i = hs.iterator();
		while(i.hasNext()){
			return i.next();
		}
		return -1;
	}
	
	public static void main(String[] args) {
		leetCode136 lc = new leetCode136();
		int[] arr = {2, 2, 1};
		lc.soluction(arr);
		int[] arr1 = {4, 1, 2, 1, 2};
		assert 4 == lc.soluction(arr1);
	}

}
