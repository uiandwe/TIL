package com.nts.algorithm;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class TreeNode {
     int val;
     TreeNode left;
     TreeNode right;
     TreeNode(int x) { val = x; }
}

public class leetCode94 {
	List<Integer> ret;
	public List<Integer> inorderTraversal(TreeNode root) {
        ret = new ArrayList<Integer>();
        traverse(root);
        return ret;
    }
	
	public void traverse(TreeNode self){
		if(self == null ) return;
		traverse(self.left);
		ret.add(self.val);
		traverse(self.right);
	}

	public static void main(String[] args) {
		leetCode94 lc = new leetCode94();
		lc.ret = new ArrayList<Integer>();
		
		System.out.println(lc.ret);
		lc.ret.add(1);
		System.out.println(lc.ret);
		System.out.println(lc.ret.get(0));
		System.out.println(lc.ret.size());
		lc.ret.clear();
		System.out.println(lc.ret.size());
		lc.ret.add(40);
		lc.ret.add(10);
		lc.ret.add(20);
		lc.ret.add(30);
		lc.ret.sort(Collections.reverseOrder());
		System.out.println(lc.ret);
		System.out.println(lc.ret.get(0));
		lc.ret.remove(0);
		System.out.println(lc.ret);
		
		
	}

}
