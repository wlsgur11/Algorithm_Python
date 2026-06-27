import java.util.*;

class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        String[] temp = s.split(" ");
        int[] sort = new int[temp.length];
        for (int i = 0; i < temp.length; i++) {
            sort[i] = Integer.parseInt(temp[i]);
        }
        Arrays.sort(sort);
        return sort[0] + " " + sort[sort.length-1];
    }
}