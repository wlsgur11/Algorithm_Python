class Solution {
    public int solution(int num1, int num2) {
        double res = (double) num1 / (double) num2 * 1000;
        System.out.println(res);
        return (int) res;
    }
}