'''
Q40 숨바꼭질

level: 2/3
'''


import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [0] + [INF] * (N)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, current = heapq.heappop(queue)

        if distance[current] < dist:
            continue

        for i in graph[current]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


dijkstra(1)

max_dist = max(distance)
count = distance.count(max(distance))
target = 0

for i, dist in enumerate(distance):
    if dist == max_dist:
        target = i
        break

print(target, max_dist, count)
