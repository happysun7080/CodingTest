### Gold 5 ###

# 1차: 221207

'''
토마토
- DFS/BFS
'''


from collections import deque

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
queue = deque([])
answer = 0

for y in range(N):
    for x in range(M):
        if graph[y][x] == 1:
            queue.append([y, x])


def bfs():
    while queue:
        y, x = queue.popleft()
        for dy, dx in zip([0, 0, 1, -1], [1, -1, 0, 0]):
            ny, nx = dy + y, dx + x

            if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                queue.append([ny, nx])


bfs()
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    answer = max(answer, max(i))
print(answer - 1)
