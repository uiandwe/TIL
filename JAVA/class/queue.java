
import java.util.*;


public class Queue {
	
	ArrayList<Integer> al = null;
	
	public Queue(){
		this.al = new ArrayList<Integer>();
	}
	
	public void push(int data){
		this.al.add(data);
	}
	
	public int size(){
		return this.al.size();
	}
	
	public boolean empty(){
		if (this.size() > 0){
			return false;
		}
		else{
			return true;
		}
	}
	
	public int pop(){
		if(this.empty() == false){
			int ret_int = this.al.get(0);
			this.al.remove(0);
			return ret_int;
			
		}
		else{
			return -1;
		}
	}
	
	
	public static void main(String[] args) {
		Queue q = new Queue();
		assert q.size() == 0 : "queue size error 1";
		
		q.push(10);
		assert q.size() == 1 : "queue size error 2";
		
		assert q.empty() == false : "queue empty error 1";
		
		q.push(20);
		q.push(10);
		
		assert q.pop() == 10 : "queue pop error 1";
		assert q.pop() == 20 : "queue pop error 2";
		assert q.pop() == 10 : "queue pop error 3";
		assert q.pop() == -1 : "queue pop error 4";
		
	}

}
