// level 3

// 1차: 221116

/**
 * 2022 KAKAO TECH INTERNSHIP - 등산코스 정하기 (118669)
 */

import java.util.*;

public class 등산코스_정하기 {
    private static List<List<Node>> graph;

    public int[] solution(int n, int[][] paths, int[] gates, int[] summits) {
        graph = new ArrayList<>();
        for (int i = 0; i < n + 1; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] path : paths) {
            int start = path[0];
            int end = path[1];
            int weight = path[2];

            if (isGate(start, gates) || isSummit(end, summits)) {
                graph.get(start).add(new Node(end, weight));
            } else if (isGate(end, gates) || isSummit(start, summits)) {
                graph.get(end).add(new Node(start, weight));
            } else {
                graph.get(start).add(new Node(end, weight));
                graph.get(end).add(new Node(start, weight));
            }
        }

        return dijkstra(n, gates, summits);
    }

    private static int[] dijkstra(int n, int[] gates, int[] summits) {
        Queue<Node> queue = new LinkedList<>();
        int[] intensity = new int[n + 1];

        Arrays.fill(intensity, Integer.MAX_VALUE);

        for (int gate : gates) {
            queue.add(new Node(gate, 0));
            intensity[gate] = 0;
        }

        while (!queue.isEmpty()) {
            Node curNode = queue.poll();

            if (curNode.weight > intensity[curNode.end]) {
                continue;
            }

            for (int i = 0; i < graph.get(curNode.end).size(); i++) {
                Node newNode = graph.get(curNode.end).get(i);

                int distance = Math.max(intensity[curNode.end], newNode.weight);
                if (intensity[newNode.end] > distance) {
                    intensity[newNode.end] = distance;
                    queue.add(new Node(newNode.end, distance));
                }
            }
        }

        int minSummit = Integer.MAX_VALUE;
        int minIntensity = Integer.MAX_VALUE;

        Arrays.sort(summits);

        for (int summit : summits) {
            if (intensity[summit] < minIntensity) {
                minSummit = summit;
                minIntensity = intensity[summit];
            }
        }

        return new int[] { minSummit, minIntensity };
    }

    private static boolean isGate(int current, int[] gates) {
        for (int gate : gates) {
            if (current == gate) {
                return true;
            }
        }
        return false;
    }

    private static boolean isSummit(int current, int[] summits) {
        for (int summit : summits) {
            if (current == summit) {
                return true;
            }
        }
        return false;
    }

    static class Node {
        int end;
        int weight;

        public Node(int end, int weight) {
            this.end = end;
            this.weight = weight;
        }
    }
}
