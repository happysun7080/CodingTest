// level 2

// 1차: 220829

/**
 * 2022 KAKAO TECH INTERNSHIP - 두 큐 합 같게 만들기 (118667)
 */

import java.util.ArrayDeque;
import java.util.Queue;

public class Solution {
    public int solution(int[] queue1, int[] queue2) {
        Queue<Integer> deque1 = new ArrayDeque<>();
        Queue<Integer> deque2 = new ArrayDeque<>();
        long sum1 = 0;
        long sum2 = 0;
        long sum;

        for (int element : queue1) {
            deque1.add(element);
            sum1 += element;
        }
        for (int element : queue2) {
            deque2.add(element);
            sum2 += element;
        }
        sum = sum1 + sum2;
        if (sum % 2 == 1)
            return -1;
        sum /= 2;

        int p1 = 0;
        int p2 = 0;
        int limit = queue1.length * 2;
        while (p1 <= limit && p2 <= limit) {
            if (sum1 == sum)
                return p1 + p2;
            if (sum1 > sum) {
                sum1 -= deque1.peek();
                sum2 += deque1.peek();
                deque2.add(deque1.poll());
                p1++;
            } else {
                sum2 -= deque2.peek();
                sum1 += deque2.peek();
                deque1.add(deque2.poll());
                p2++;
            }
        }
        return -1;
    }
}
