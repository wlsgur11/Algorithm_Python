class Solution {
    public int[] solution(int[] arr) {
        if (arr.length == 1) return new int[] {-1};
        int mini = arr[0];
        for (int i: arr) mini = Math.min(mini, i);
        
        int idx = 0;
        int[] ans = new int[arr.length - 1];
        for (int i = 0; i < arr.length; i++) if (arr[i] != mini) ans[idx++] = arr[i];
        return ans;
    }
}