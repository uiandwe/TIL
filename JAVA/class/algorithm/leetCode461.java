package com.nts.algorithm;

public class leetCode461 {

	public static void main(String[] args) {
		int x = 1;
		int y = 4;
		int xor = x ^ y;
		int cur = 0;
		for(int i=0; i<32; i++){
			cur += (xor >> i)  & 1; 
		}
		
		System.out.println(cur);

	}

}
