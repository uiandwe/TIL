package com.nts.algorithm;

import java.util.Stack;

public class leetCode20 {
	
	public boolean isValid(String s) {
		Stack<Character> stack = new Stack<>();
		char[] arr = s.toCharArray();
		for(char c : arr){
			if(c == '(' || c == '{' || c == '['){
				stack.push(c);
			}
			else if(c == ')'){
				if(stack.size() != 0 && stack.pop() != '('){
					return false;
				}
			}
			else if(c == ']'){
				if(stack.size() != 0 && stack.pop() != '['){
					return false;
				}
			}
			else if(c == '}'){
				if(stack.size() != 0 && stack.pop() != '{'){
					return false;
				}
			}
			else{
				return false;
			}
		}
		if(stack.size() > 0){
			return false;
		}
		else{
			return true;
		}
    }


	public static void main(String[] args) {
		leetCode20 l = new leetCode20();
		assert true == l.isValid("()");
		assert true == l.isValid("()[]{}");
		assert false == l.isValid("([]{}");
		assert true == l.isValid("({})");

	}

}
