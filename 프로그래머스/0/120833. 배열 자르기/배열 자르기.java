import java.util.*;

class Solution {
    public int[] solution(int[] numbers, int num1, int num2) {
        ArrayList<Integer> answer = new ArrayList<>();
        for (int i = num1; i <= num2; i++){
            answer.add(numbers[i]);
        }
        int[] res = new int[answer.size()];
        for (int j = 0; j < answer.size();j ++){
            res[j] = answer.get(j);
        }
        return res;
    }
}