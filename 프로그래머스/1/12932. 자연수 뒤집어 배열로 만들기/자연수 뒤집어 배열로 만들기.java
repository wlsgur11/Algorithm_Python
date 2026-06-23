class Solution {
    public int[] solution(long n) {
        StringBuilder sb = new StringBuilder(Long.toString(n)).reverse();
        int[] arr = new int[sb.length()];
        for (int i = 0; i < sb.length(); i++) {
            arr[i] = sb.charAt(i) - '0';
        }
        return arr;
    }
}