package com.nts.algorithm;

import java.util.LinkedList;
import java.util.Queue;

public class dijkstraDemo {

	int[][] d = null;
	int[] visite = null;
	int[] node_weight = null;
	Queue<Integer> q = null;
	
	public void dPrint(){
		for (int i = 0; i < visite.length; i++) {
			System.out.print(visite[i]+"\t");
		}
		
		System.out.println("");
		
		for (int i = 0; i < node_weight.length; i++) {
			System.out.print(node_weight[i]+"\t");
		}
		System.out.println("");
	}
	
	public int dijkstra(int[][] nodes, int cnt_node, int start_node, int end_node){
		initWeight();
		q.offer(start_node);
		node_weight[start_node] = 0;
		
		while(q.isEmpty() == false){
			int now_node = q.poll();
			visite[now_node] = 1;
			
			for(int i=0; i<cnt_node+1; i++){
				if(d[now_node][i] > 0 && visite[i] == 0){
					q.offer(i);
					if(node_weight[now_node]+d[now_node][i] < node_weight[i]){
						node_weight[i] = node_weight[now_node]+d[now_node][i];
					}
				}
			}
		}
		dPrint();
		return node_weight[end_node];
	}
	
	public void initWeight(){
		for(int i=0; i<node_weight.length; i++){
			node_weight[i] = Integer.MAX_VALUE;
		}
		
		for(int i=0; i<visite.length; i++){
			visite[i] = 0;
		}
	}
	
	dijkstraDemo(int cnt_node, int[][] nodes){
		d = new int[cnt_node+1][cnt_node+1];
		visite = new int[cnt_node+1];
		node_weight = new int[cnt_node+1];
		q = new LinkedList<Integer>();
	
		for(int[] node : nodes){
			int start_node = node[0];
			int end_node = node[1];
			int weight = node[2];
			
			d[start_node][end_node] = weight;
		}
	}
	
	
	public static void main(String[] args) {
		int[][] nodes = {
				{1, 2, 2},
				{1, 3, 1},
				{1, 4, 1},
				{2, 3, 4},
				{2, 6, 3},
				{3, 5, 4},
				{3, 6, 1},
				{4, 5, 4},
				{5, 7, 4},
				{6, 5, 2},
				{6, 7, 7}
		};
		int cnt_node = 7;
		dijkstraDemo dd = new dijkstraDemo(cnt_node, nodes);
		System.out.println(dd.dijkstra(nodes, cnt_node, 1, 7));
		System.out.println(dd.dijkstra(nodes, cnt_node, 2, 5));
		System.out.println(dd.dijkstra(nodes, cnt_node, 2, 4));

	}

}
