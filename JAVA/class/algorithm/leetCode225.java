package com.nts.algorithm;

import java.util.LinkedList;
import java.util.Queue;

class MyStack {

	Queue<Integer> q = null;
    /** Initialize your data structure here. */
    public MyStack() {
        q = new LinkedList<>();
    }
    
    /** Push element x onto stack. */
    public void push(int x) {
        int queue_size = q.size();
        q.offer(x);
        for(int i=0; i<queue_size; i++){
        	int temp = q.poll();
        	q.offer(temp);
        }
    }
    
    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        return q.poll();
    }
    
    /** Get the top element. */
    public int top() {
        return q.peek();
    }
    
    /** Returns whether the stack is empty. */
    public boolean empty() {
        return q.isEmpty();
    }
}


public class leetCode225 {

	public static void main(String[] args) {
		MyStack stack = new MyStack();

		stack.push(1);
		stack.push(2);  
		assert 2 == stack.top();   // returns 2
		assert 2 == stack.pop();   // returns 2
		assert false == stack.empty(); // returns false

	}

}
