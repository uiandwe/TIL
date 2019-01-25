
import java.util.*;

public class Stack {
	
	ArrayList<Integer> al = null;
	
	public Stack(){
		this.al = new ArrayList<Integer>();
	}
	
	public void push(int data){
		this.al.add(data);
	}
	
	public int size(){
		return this.al.size();
	}
	
	public Boolean empty(){
		if(this.size() > 0){
			return false;
		}
		else{
			return true;
		}
	}
	
	public int pop(){
		if(this.empty() == false){
			int ret_Int = this.al.get(this.al.size()-1);
			this.al.remove(this.al.size()-1);
			return ret_Int; 
		}
		else{
			return -1;
		}
	}
	
	
	public static void main(String[] args) {
		Stack s1 = new Stack();
		s1.push(1);
		s1.push(2);
		s1.push(3);
		
		while(s1.empty() == false){
			System.out.println(s1.pop());
		}

	}

}
