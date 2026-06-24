class Solution {
    boolean solution(String s) {
        s = s.toUpperCase();
        int a = 0;
        int b = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == 'P') a++;
            if (c == 'Y') b++;
        }
        return a == b;
    }
}