import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] ans = new int[commands.length];
        
        for (int a = 0; a < commands.length; a++) {
            int i = commands[a][0] - 1;
            int j = commands[a][1];
            int k = commands[a][2];
            int[] temp = Arrays.copyOfRange(array, i, j);
            Arrays.sort(temp);
            
            ans[a] = temp[k-1];
        }
        return ans;
    }
}