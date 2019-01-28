package com.nts.algorithm;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Node{
	int val = 0;
	Node next = null;
	
	Node(int data){
		val = data;
	}
}

class bNode{
	int val = 0;
	bNode left = null;
	bNode right = null;
	bNode(int data){
		val = data;
	}
}

class QuickSort1{
	Node root = null;
	bNode broot = null;
	
	public void sort(int[] nums, int left, int right) {
		if(nums.length<=1) {
			return ;
		}
		
		int i, j, temp, pivot;
		i = left;
		j = right;
		
		while(i<j) {
			pivot = nums[(left+right)/2];
			while(pivot < nums[j]) j--;
			while(i<j && nums[i] < pivot) i++;
			
			temp = nums[i];
			nums[i] = nums[j];
			nums[j] = temp;
			
			sort(nums, left, i-1);
			sort(nums, i+1, right);
		}
		
	}
	
	
	public int search(int[] nums, int data) {
		int left = 0;
		int right = nums.length-1;
		
		while(left <= right) {
			int mid = (left+right)/2;
			if(nums[mid] == data) {
				return mid;
			}
			else if(nums[mid] < data) {
				left = mid+1;
			}
			else {
				right = mid-1;
			}
		}
		
		return -1;
	}
	
	public Node createTree(Node n, int  data) {
		if(n == null) {
			n = new Node(data);
		}
		else {
			n.next = createTree(n.next, data);
		}
		
		return n;
	}
	
	public void Tree(int data) {
		root = createTree(root, data);
	}
	
	
	public bNode createbTree(bNode n, int data) {
		if(n == null) {
			n = new bNode(data);
		}
		else {
			if(n.val > data) {
				n.left = createbTree(n.left, data);
			}
			else {
				n.right = createbTree(n.right, data);
			}
		}
		return n;
	}
	
	
	public void bTree(int data) {
		broot = createbTree(broot, data);
	}
	
	
	public void inOrder(bNode n, List<Integer> ret) {
		if(n == null) {
			return;
		}
		else {
			if(n.left != null) inOrder(n.left, ret);
			ret.add(n.val);
			if(n.right != null) inOrder(n.right, ret);
		}
	}
	
	public void dfs(bNode root, List<Integer> ret) {
		if(root == null) {
			return;
		}
		else {
			Queue<bNode> q = new LinkedList<>();
			q.offer(root);
			
			while(!q.isEmpty()) {
				bNode temp = q.poll();
				ret.add(temp.val);
				
				if(temp.left != null) q.offer(temp.left);
				if(temp.right != null) q.offer(temp.right);
			}
		}
	}
}

public class testDemo {

	public static void main(String[] args) {
		QuickSort1 q = new QuickSort1();
		int[] nums = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
		q.sort(nums, 0, nums.length-1);
		for(int num:nums) {
			System.out.print(num+"\t");
		}
		System.out.println("\n----------------");
		System.out.println(q.search(nums, 1));

		q.Tree(10);
		System.out.println(q.root.val);
		q.Tree(20);
		System.out.println(q.root.next.val);
		System.out.println(q.root.val);
		q.Tree(30);
		System.out.println(q.root.next.next.val);
		System.out.println("\n----------------");
		
		q.bTree(10);
		System.out.println(q.broot.val);
		q.bTree(20);
		System.out.println(q.broot.val);
		System.out.println(q.broot.right.val);
		q.bTree(5);
		q.bTree(1);
		q.bTree(15);
		q.bTree(50);
		System.out.println(q.broot.left.val);
		
		List<Integer> al = new ArrayList();
		q.inOrder(q.broot, al);
		Iterator<Integer> it = al.iterator();
		while(it.hasNext()) {
			System.out.print(it.next()+"\t");
		}
		
		System.out.println("\n----------------");
		
		List<Integer> al2 = new ArrayList();
		q.dfs(q.broot, al2);
		Iterator<Integer> it2 = al2.iterator();
		while(it2.hasNext()) {
			System.out.print(it2.next()+"\t");
		}
	}

}
