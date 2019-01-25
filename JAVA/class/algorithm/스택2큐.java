package com.nts.algorithm;

import java.util.Scanner;
import com.nts.test.Stack;

public class stackMakeQueue {

	@SuppressWarnings("resource")
	public static void main(String[] args) {
		Stack s1 = new Stack();
		Stack s2 = new Stack();
		
		Scanner sc = new Scanner(System.in);
		while(sc.hasNext()){
			int temp_val = sc.nextInt();
			s1.push(temp_val);
			
			while(s1.empty() == false){
				s2.push(s1.pop());
			}
			
			while(s2.empty() == false){
				int ret_val = s2.pop();
				System.out.println(ret_val);
				s1.push(ret_val);
			}
		}
		

	}

}
