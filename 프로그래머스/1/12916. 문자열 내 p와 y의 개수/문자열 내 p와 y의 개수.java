class Solution {
    boolean solution(String s) {
        s = s.toUpperCase();
        int P_cnt = 0;
        int Y_cnt = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'P') P_cnt += 1;
            else if (s.charAt(i) == 'Y') Y_cnt += 1;
        }
        if (P_cnt == Y_cnt) return true;
        else return false;
    }
}