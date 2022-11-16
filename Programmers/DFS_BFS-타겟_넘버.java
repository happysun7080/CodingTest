// level 2

// 1차: 221116

/**
 * DFS/BFS - 타겟 넘버 (43165)
 */

public class 타겟_넘버 {
    private int answer;
    private int length;

    public int solution(int[] numbers, int target) {
        answer = 0;
        length = numbers.length;
        dfs(0, 0, numbers, target);
        return answer;
    }

    private void dfs(int current, int index, int[] numbers, int target) {
        if (index < length) {
            dfs(current + numbers[index], index + 1, numbers, target);
            dfs(current - numbers[index], index + 1, numbers, target);
        }
        if (index == length && current == target) {
            answer++;
        }
    }
}
