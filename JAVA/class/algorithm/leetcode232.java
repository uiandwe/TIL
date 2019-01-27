package com.nts.algorithm;

import java.util.Stack;

class MyQueue {
    Stack<Integer> in = null;
    Stack<Integer> out = null;
    /** Initialize your data structure here. */
    public MyQueue() {
    	in = new Stack<>();
    	out = new Stack<>();
    }
    
    /** Push element x to the back of queue. */
    public void push(int x) {
    	
    	while(out.empty() == false){
    		in.push(out.pop());
    	}
    	in.push(x);
    	
        while(in.empty() == false){
        	out.push(in.pop());
        }
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
    	return out.pop();
    }
    
    /** Get the front element. */
    public int peek() {
    	if(empty()){
    		return -1;
    	}
    	else{
    		return out.peek();
    	}
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() {
        return out.isEmpty();
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
