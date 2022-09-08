'''
Q17 경잭적 전염

level: 2/3
reference: Baekjoon 18405
'''


from collections import deque


N, K = map(int, input().split())
graph, _deq = [], []
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] != 0:
            _deq.append((graph[i][j], 0, i, j))
S, X, Y = map(int, input().split())

_deq.sort()
deq = deque(_deq)

# BFS
while deq:
    virus, s, x, y = deq.popleft()
    if s == S:
        break
    for dy, dx in zip([0, 0, 1, -1], [1, -1, 0, 0]):
        _y, _x = y + dy, x + dx
        if 0 <= _y < N and 0 <= _x < N:
            if graph[_x][_y] == 0:
                graph[_x][_y] = virus
                deq.append((virus, s+1, _x, _y))

print(graph[X-1][Y-1])
