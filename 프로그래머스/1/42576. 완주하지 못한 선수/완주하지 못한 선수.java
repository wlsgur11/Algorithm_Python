import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        // 해시맵 생성 participant로
        HashMap<String, Integer> map = new HashMap<>();
        for (String player: participant)
            map.put(player, map.getOrDefault(player, 0) + 1);
        
        // 해시맵 수정 completion으로 - 1
        for (String player: completion)
            map.put(player, map.get(player) - 1);
        
        // 0이 아닌 keySet에서 찾기
        for (String key: map.keySet()) 
            if (map.get(key) != 0) 
                return key;
        return "";

    }
}