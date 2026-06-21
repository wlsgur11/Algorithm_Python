    class Solution {
        public String solution(String phone_number) {
            String ans = "";
            for (int i = 0; i < phone_number.length()-4; i++) {
                ans += "*";
            }
            return ans + phone_number.substring(phone_number.length()-4);
        }
    }