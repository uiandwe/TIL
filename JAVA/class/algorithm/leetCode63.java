package com.nts.algorithm;


class Solution63 {
	public int uniquePathsWithObstacles(int[][] obstacleGrid) {
		int map_m_len = obstacleGrid.length;
		int map_n_len = obstacleGrid[0].length;
		
		int[][] d2 = new int[map_m_len][map_n_len];
		
		d2[0][0] = 1;
		
		for (int i = 0; i < map_m_len; i++) {
			for (int j = 0; j < map_n_len; j++) {
				if(obstacleGrid[i][j] == 1){
					d2[i][j] = 0;
				}
				else{
					if(i-1>=0) d2[i][j] += d2[i-1][j];
					if(j-1>=0) d2[i][j] += d2[i][j-1];
				}
			}
		}
		
		
		for(int i=0; i<map_m_len; i++){
			for(int j=0; j<map_n_len; j++){
				System.out.print(d2[i][j] +"\t");
			}
			System.out.println();
		}
		
		return d2[map_m_len-1][map_n_len-1];
    }
}


public class leetCode63 {

	public static void main(String[] args) {
		Solution63 s = new Solution63();
		int[][] map = {
				{0, 0, 0},
				{0, 1, 0},
				{0, 0, 0}
		};
		s.uniquePathsWithObstacles(map);

		int[][] map1 = {
				{1}
		};
		s.uniquePathsWithObstacles(map1);
		
		int[][] map2 = {
				{0}
		};
		s.uniquePathsWithObstacles(map2);
	}

}
