class Solution {
    public long solution(int a, int b) {
        long res = 0L;
        if (a>b){
            for (int i = b; b <= a; b++) {
                res += b;
            }
        }
        else {
            for (int i = a; a <= b; a++) {
                res += a;
            }
        }
    return res;
    }
}