class Solution {
    public String solution(String new_id) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < new_id.length(); i++) {
            sb.append(Character.toLowerCase(new_id.charAt(i)));
        }

        StringBuilder temp = new StringBuilder();
        for (int i = 0; i < sb.length(); i++) {
            char c = sb.charAt(i);

            if (Character.isLetterOrDigit(c)
                    || c == '-'
                    || c == '_'
                    || c == '.') {
                temp.append(c);
            }
        }
        sb = temp;

        temp = new StringBuilder();
        for (int i = 0; i < sb.length(); i++) {
            char c = sb.charAt(i);

            if (c == '.') {
                if (temp.length() > 0 && temp.charAt(temp.length() - 1) == '.') {
                    continue;
                }
            }

            temp.append(c);
        }
        sb = temp;

        while (sb.length() > 0 && sb.charAt(0) == '.') {
            sb.deleteCharAt(0);
        }

        while (sb.length() > 0 && sb.charAt(sb.length() - 1) == '.') {
            sb.deleteCharAt(sb.length() - 1);
        }

        if (sb.length() == 0) {
            sb.append('a');
        }

        if (sb.length() >= 16) {
            sb.setLength(15);

            if (sb.charAt(sb.length() - 1) == '.') {
                sb.deleteCharAt(sb.length() - 1);
            }
        }

        while (sb.length() < 3) {
            sb.append(sb.charAt(sb.length() - 1));
        }

        return sb.toString();
    }
}