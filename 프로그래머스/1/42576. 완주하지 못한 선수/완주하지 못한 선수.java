import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        // 1. 해십ㅁ맵을 만든다
        HashMap<String, Integer> map = new HashMap<>();
        for (String player: participant)
            map.put(player, map.getOrDefault(player, 0) + 1);
        
        // 2. 해시맵에 participant를 뺀다
        for (String player: completion)
            map.put(player, map.get(player) - 1);
        // 4. value가 0이 아닌 사람을 찾는다
        for (String key: map.keySet())
            if (map.get(key) != 0)
                return key;
        return "";
    }
}