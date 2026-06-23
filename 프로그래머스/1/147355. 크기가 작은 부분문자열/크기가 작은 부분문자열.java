class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        int n = p.length();
        long ab = Long.parseLong(p);
        for (int i = 0; i <= t.length() - n; i++) {
            long num = Long.parseLong(t.substring(i, i+n));
            if (num <= ab) answer++;
        }
        return answer;
    }
}