package com.nts.algorithm;

import java.util.ArrayList;
import java.util.List;

public class leetCode784 {
	List<String> ret = null;
	
	
	public void backTracing(char[] arr, int i){
		if(i == arr.length){
			ret.add(new String(arr));
		}
		else{
			char c = arr[i];
			if(Character.isDigit(c)){
				backTracing(arr, i+1);
			}
			else{
				arr[i] = Character.toLowerCase(c);
				backTracing(arr, i+1);
				arr[i] = Character.toUpperCase(c);
				backTracing(arr, i+1);
			}
		}
	}
	
	public List<String> letterCasePermutation(String S) {
		ret = new ArrayList<>();
		char[] arr = S.toCharArray();
		backTracing(arr, 0);
				
		return ret;
				
    }


	public static void main(String[] args) {
		leetCode784 lc = new leetCode784();
		lc.letterCasePermutation("a1b2");
		System.out.println(lc.ret);

	}

}
