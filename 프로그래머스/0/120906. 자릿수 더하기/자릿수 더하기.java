class Solution {
    public int solution(int n) {
        int ans = 0;
        while (true) {
            if (n / 10 < 1) {
                ans += n % 10;
                return ans;
            }
            ans += n % 10;
            n = n / 10;
        }
    }
}