class Solution {
    public int[] solution(long n) {
        StringBuilder sb = new StringBuilder(String.valueOf(n)).reverse();
        int[] ans = new int[sb.length()];
        for (int i = 0; i < sb.length(); i++) ans[i] = sb.charAt(i) - '0';
        return ans;
    }
}