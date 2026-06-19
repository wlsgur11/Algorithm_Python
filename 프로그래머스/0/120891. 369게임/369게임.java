class Solution {
    public int solution(int order) {
        int answer = 0;
        while (true) {
            if (order % 10 == 3 || order % 10 == 6 || order % 10 == 9){
                    answer++;
                }
            if (order / 10 == 0) {
                break;
            }
            order = order / 10;
        }
        return answer;
    }
}