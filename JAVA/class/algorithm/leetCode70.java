package com.nts.algorithm;

public class leetCode70 {
	
	public int climbStairs(int n) {
		if(n == 0 || n == 1){
			return 1;
		}
		
		int[] d = new int[n+1];
		d[0] = 1;
		d[1] = 1;
		
		for(int i=2; i<=n; i++){
			d[i] = d[i-2]+d[i-1];
		}
		
		return d[n];
    }

	public static void main(String[] args) {
		leetCode70 l = new leetCode70();
		assert 2 == l.climbStairs(2);
		assert 3 == l.climbStairs(3);
		assert 5 == l.climbStairs(4);
		assert 8 == l.climbStairs(5);
	}

}
