### Silver 2 ###

# 1차: 220901

'''
유기농 배추
- 그래프
- DFS/BFS
'''


from collections import deque


def bfs(graph, i, j, N, M):
    deq = deque()
    deq.append((i, j))
    graph[i][j] = -1

    while deq:
        y, x = deq.popleft()
        for dy, dx in zip([0, 0, 1, -1], [1, -1, 0, 0]):
            _y, _x = y+dy, x+dx
            if _y < 0 or _y >= N or _x < 0 or _x >= M:
                continue
            if graph[_y][_x] == 1:
                graph[_y][_x] = -1
                deq.append((_y, _x))
    return


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    answer = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(graph, i, j, N, M)
                answer += 1
    print(answer)
