package com.nts.algorithm;

class Solution64 {
    public int minPathSum(int[][] grid) {
    	int m = grid.length; 
    	int n = grid[0].length;
    	
        for(int i=0; i<m; i++){
        	for(int j=0; j<n; j++){
        		if(i == 0 && j == 0){
        			continue;
        		}
        		
        		int temp = Integer.MAX_VALUE;
        		if(i-1>=0) temp = Math.min(temp, grid[i-1][j]);
        		if(j-1>=0) temp = Math.min(temp, grid[i][j-1]);
        		grid[i][j] += temp; 
        	}
        }
        
        return grid[m-1][n-1];
    }
}

public class leetCode64 {
	public static void main(String[] args) {
		Solution64 s = new Solution64();
		int[][] grid = {
				{1, 3, 1},
				{1, 5, 1},
				{4, 2, 1},
		};
		assert 7 == s.minPathSum(grid);
	}
}
