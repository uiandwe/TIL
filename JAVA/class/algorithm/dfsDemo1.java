package com.nts.algorithm;

public class dfsDemo1 {

	static int[][] d = null;
	static int[][] visite = null;
	static int m = 0;
	static int n = 0;
	
	public static void dfs(int[][] map, int x, int y, int step){
		if(x == m-1 && y == n-1){
			d[x][y] = Math.min(step, d[x][y]);
			return;
		}
		else{
			d[x][y] = step;
			visite[x][y] = 1;
			
			int[] position_x = {-1, 1, 0, 0};
			int[] position_y = {0, 0, 1, -1};
			
			for(int i=0; i<4; i++){
				int next_x = x + position_x[i];
				int next_y = y + position_y[i];
				if(next_x >=0 && next_x < m && next_y >= 0 && next_y < n){
					if(map[next_x][next_y] == 1 && visite[next_x][next_y] == 0){
						dfs(map, next_x, next_y, step+1);
					}
				}
			}
		}
	}
	
	public static void main(String[] args) {
//		int[][] map = {
//				{1, 1, 1}
//		};
		
//		int[][] map = {
//				{1, 1, 1},
//				{1, 0, 1},
//				{1, 1, 1}
//		};
		
		int[][] map = {
				{1, 1, 1, 1, 1},
				{1, 0, 1, 1, 1},
				{1, 1, 1, 1, 1}
		};
		
		m = map.length;
		n = map[0].length;
		d = new int[m][n];
		d[m-1][n-1] = Integer.MAX_VALUE;
		
		visite = new int[m][n];
		
		for(int i=0; i<m; i++){
			for(int j=0; j<n; j++){
				if(map[i][j] == 1 && visite[i][j] == 0 && (i != m-1 && j != n-1)){
					dfs(map, i, j, 1);
				}
			}
		}
		
		for(int i=0; i<m; i++){
			for(int j=0; j<n; j++){
				System.out.print(d[i][j]+ "\t");
			}
			System.out.println();
		}

	}

}
