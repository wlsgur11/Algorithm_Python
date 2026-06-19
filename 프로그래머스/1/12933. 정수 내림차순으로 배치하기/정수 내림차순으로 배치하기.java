import java.util.*;

class Solution {
    public long solution(long n) {
        String s = n+"";
        char [] chars = s.toCharArray();
        Arrays.sort(chars);
        
        StringBuilder sb = new StringBuilder(new String (chars));
        String res = sb.reverse().toString();
        return Long.parseLong(res);
    }
}