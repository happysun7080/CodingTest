// level 1

// 1차: 221108

/**
 * 2022 KAKAO TECH INTERNSHIP - 성격 유형 검사하기 (118666)
 */

import java.util.HashMap;
import java.util.Map;

public class Solution {
    public String solution(String[] survey, int[] choices) {
        Map<Character, Integer> score = new HashMap<>();
        int choice;
        char key;

        for (int i = 0; i < survey.length; i++) {
            choice = choices[i] - 4;
            if (choice > 0) {
                key = survey[i].charAt(1);
            } else if (choice < 0) {
                key = survey[i].charAt(0);
            } else {
                continue;
            }
            score.put(key, score.getOrDefault(key, 0) + Math.abs(choice));
        }

        StringBuilder answer = new StringBuilder();
        char first, second;
        for (String type : new String[] { "RT", "CF", "JM", "AN" }) {
            first = type.charAt(0);
            second = type.charAt(1);
            if (score.getOrDefault(first, 0) > score.getOrDefault(second, 0)) {
                answer.append(first);
            } else if (score.getOrDefault(first, 0) < score.getOrDefault(second, 0)) {
                answer.append(second);
            } else {
                answer.append(first - second < 0 ? first : second);
            }
        }
        return answer.toString();
    }
}