### Gold 3 ###

# 1차: 221124

'''
파티
- 그래프
- 다익스트라
'''


import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))


def dijkstra(start):
    queue = []
    distance = [INF for _ in range(N+1)]

    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        cur_cost, cur = heapq.heappop(queue)

        if distance[cur] < cur_cost:
            continue

        for v_end, v_cost in graph[cur]:
            cost = cur_cost + v_cost

            if distance[v_end] > cost:
                distance[v_end] = cost
                heapq.heappush(queue, (cost, v_end))

    return distance


result = 0
for i in range(1, N+1):
    departure = dijkstra(i)
    get_off = dijkstra(X)
    result = max(result, departure[X] + get_off[i])

print(result)
