import java.math.*;

class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        int c = Math.min(a, b);
        int d = Math.max(a, b);
        for (int i = c;i <= d; i++){
            answer += i;
        }
        return answer;
    }
}