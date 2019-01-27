package com.nts.algorithm;

import java.util.Stack;

class MyQueue {
    Stack<Integer> s1 = null;
    Stack<Integer> s2 = null;
    /** Initialize your data structure here. */
    public MyQueue() {
    	s1 = new Stack<>();
    	s2 = new Stack<>();
    }
    
    /** Push element x to the back of queue. */
    public void push(int x) {
    	
    	while(s2.empty() == false){
    		s1.push(s2.pop());
    	}
    	s1.push(x);
    	
        while(s1.empty() == false){
        	s2.push(s1.pop());
        }
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
    	return s2.pop();
    }
    
    /** Get the front element. */
    public int peek() {
    	return s2.peek();
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() {
        if(s2.size() > 0){
        	return false;
        }
        else{
        	return true;
        }
    }
}


public class leetCode232 {

	public static void main(String[] args) {
		 MyQueue obj = new MyQueue();
		 obj.push(1);
		 obj.push(2);
		 assert 1 == obj.peek();
		 assert 1 == obj.pop();
		 assert 2 == obj.peek();
		 assert false == obj.empty();
		 
	}

}
