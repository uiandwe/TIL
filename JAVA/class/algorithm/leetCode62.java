package com.nts.algorithm;


class Solution62 {
    public int uniquePaths(int m, int n) {
        int[][] d = new int[n][m];
        for(int i=0; i<n; i++){
        	d[i][0] = 1;
        }
        
        for(int i=0; i<m; i++){
        	d[0][i] = 1;
        }
        
        for(int i=1; i<n; i++){
        	for(int j=1; j<m; j++){
        		d[i][j] = d[i-1][j]+d[i][j-1];
        	}
        }
        return d[n-1][m-1];
    }
}


public class leetCode62 {

	public static void main(String[] args) {
		Solution62 s = new Solution62();
		assert 3 == s.uniquePaths(3, 2);
		assert 28 == s.uniquePaths(7, 3);

	}

}
