class Solution {
    public boolean solution(int x) {
        int res = 0;
        int tmp = x;
        while (tmp > 0) {
            res += tmp % 10;
            tmp /= 10;
        }
        if (x % res == 0) return true;
        else return false;
    }
}