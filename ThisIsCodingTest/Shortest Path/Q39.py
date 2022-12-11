'''
Q39 화성 탐사

level: 2/3
'''


import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

for _ in range(int(input())):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    distance = [[INF] * N for _ in range(N)]

    x, y = 0, 0
    queue = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    while queue:
        dist, x, y = heapq.heappop(queue)

        if distance[x][y] < dist:
            continue

        for _x, _y in zip(dx, dy):
            nx, ny = x + _x, y + _y

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            cost = dist + graph[nx][ny]

            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(queue, (cost, nx, ny))

    print(distance[N-1][N-1])
