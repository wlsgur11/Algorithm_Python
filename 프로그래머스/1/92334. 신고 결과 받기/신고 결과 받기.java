import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        // 중복 신고 제거하기
        HashSet<String> reportSet = new HashSet<>(Arrays.asList(report));
        
        // 신고당한 횟수 기록
        HashMap<String, Integer> reportedMap = new HashMap<>();
        for (String rep: reportSet){
            String name = rep.split(" ")[1];
            reportedMap.put(name, reportedMap.getOrDefault(name, 0) + 1);            
        }     
        
        // 내가 신고한 사람 중 정지 된 사람이 몇명인지
        HashMap<String, Integer> mailCountMap = new HashMap<>();
        
        for (String rep: reportSet){
            String[] name = rep.split(" ");
            String reporter = name[0];
            String reported = name[1];
            
            if (reportedMap.get(reported) >= k){
                mailCountMap.put(reporter, mailCountMap.getOrDefault(reporter, 0) + 1);
            }
        }
        
        // 결과 배열 만들기
        int[] ans = new int[id_list.length];
        
        for (int i = 0; i < id_list.length; i++){
            ans[i] = mailCountMap.getOrDefault(id_list[i], 0);
        }
        
        return ans;
        
    }
}