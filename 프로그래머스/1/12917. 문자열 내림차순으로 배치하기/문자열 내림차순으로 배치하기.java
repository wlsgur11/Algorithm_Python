import java.util.*;

class Solution {
    public String solution(String s) {
        // string -> array
        char[] arr = s.toCharArray();
        
        // sort
        Arrays.sort(arr);
        
        String data = new String(arr);
        // StringBuilder().reverse().toString()
        
        return new StringBuilder(data).reverse().toString();
        
    }
}