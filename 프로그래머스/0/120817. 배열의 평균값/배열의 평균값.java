class Solution {
    public double solution(int[] numbers) {
        double res = 0.0f;
        int sum = 0;
        for (int i: numbers) {
            sum += i;
        }
        res = (double) sum / numbers.length;
        return res;
    }
}