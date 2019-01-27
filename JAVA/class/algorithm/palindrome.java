package com.nts.algorithm;

public class palindrome {

	public static boolean palindrom(String str){
		int len = str.length()-1;
		
		for(int i=0; i<=len/2; i++){
			if(str.charAt(i) != str.charAt(len-i)){
				return false;
			}
		}
		return true;
	}
	
	public static void main(String[] args) {
		String str = "lol";
		System.out.println(palindrom(str));
		
		String str1 = "loll";
		System.out.println(palindrom(str1));
		

	}

}
