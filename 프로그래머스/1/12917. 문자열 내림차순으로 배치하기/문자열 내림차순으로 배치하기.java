import java.util.Arrays;

class Solution {
    public String solution(String s) {
        char[] arr = s.toCharArray();
        Arrays.sort(arr);
        String data = new String(arr);
        
        return new StringBuilder(data).reverse().toString();
    }
}