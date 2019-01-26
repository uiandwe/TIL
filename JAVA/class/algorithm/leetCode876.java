package com.nts.algorithm;

class ListNode {
	      int val;
	      ListNode next;
	      ListNode(int x) { val = x; }
}

public class leetCode876 {

	public ListNode middleNode(ListNode head) {
		return head;
    }

	public ListNode initListNode(int range){
		ListNode ln = null;
		for(int i=0; i<=range; i++){
			if(ln == null){
				ln = new ListNode(i);
			}
			else{
				ListNode tempLn = new ListNode(i);
				ListNode temp = ln;
				while(temp.next != null){
					temp = temp.next;
				}
				temp.next = tempLn;
			}
		}
		
		return ln;
	}
	
	
	public ListNode soluction(ListNode head){
		ListNode walker = head;
		ListNode runner = head;
		
		while(runner != null){
			runner = runner.next;
			if(runner!= null){
				walker = walker.next;
				runner = runner.next;
			}
		}
		return walker;
	}
	
	public static void main(String[] args) {
		
		leetCode876 lc = new leetCode876();
		ListNode ln = lc.initListNode(5);
		
		ListNode ret = lc.soluction(ln);
		
		while(ret != null){
			System.out.println(ret.val);
			ret = ret.next;
		}
	}

}
