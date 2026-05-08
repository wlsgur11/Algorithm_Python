import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        boolean[][] visited = new boolean[n][m];
        
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[] {0, 0, 1});
        visited[0][0] = true;
        
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, 1, -1};
        
        while (!q.isEmpty()){
            int[] curr = q.poll();
            int x = curr[0];
            int y = curr[1];
            int dist = curr[2];
            
            if (x == n-1 && y == m-1) return dist;
            
            for (int i = 0; i< 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && maps[nx][ny] == 1 && !visited[nx][ny]){
                    q.add(new int[] {nx, ny, dist+1});
                    visited[nx][ny] = true;
                }
            }
        }
        return -1;
    }
}