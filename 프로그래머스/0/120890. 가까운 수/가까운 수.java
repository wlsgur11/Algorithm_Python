class Solution {
    public int solution(int[] array, int n) {
        int answer = array[0];
        int minDiff = Math.abs(array[0] - n);
        
        for (int i: array){
            int diff = Math.abs(i-n);
            
            if (diff < minDiff){
                minDiff = diff;
                answer = i;
            }
            else if (minDiff == diff && i < answer){
                answer = i;
            }
        }
        return answer;
    }
}