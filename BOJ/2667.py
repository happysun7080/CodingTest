### Silver 1 ###

# 1차: 221205

'''
단지번호붙이기
- DFS/BFS
'''


from collections import deque

N = int(input())
graph = [[int(i) for i in input().rstrip()] for _ in range(N)]
visited = [[False] * N for _ in range(N)]


def bfs(y, x):
    global graph, visited

    count = 0
    queue = deque()
    queue.append([y, x])

    while queue:
        ny, nx = queue.popleft()
        count += 1

        for dy, dx in zip([0, 0, 1, -1], [1, -1, 0, 0]):
            if 0 <= ny + dy < N and 0 <= nx + dx < N:
                if not visited[ny + dy][nx + dx] and graph[ny + dy][nx + dx] == 1:
                    queue.append([ny + dy, nx + dx])
                    visited[ny + dy][nx + dx] = True

    return count


counts = []

for y in range(N):
    for x in range(N):
        if not visited[y][x] and graph[y][x] == 1:
            visited[y][x] = True
            counts.append(bfs(y, x))

print(len(counts))
for count in sorted(counts):
    print(count)
