class Solution {
    public double solution(int[] numbers) {
        float res = 0.0f;
        int sum = 0;
        for (int i: numbers) {
            sum += i;
        }
        res = (float) sum / numbers.length;
        return res;
    }
}