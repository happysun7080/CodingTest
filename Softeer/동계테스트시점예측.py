'''
level: 3/5 - 동계 테스트 시점 예측
'''


import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


def isComplete(_graph):
    for row in _graph:
        if 1 in row:
            return False

    return True


def getExternal(_graph):
    global N, M

    deq = deque([(0, 0)])
    external = set([(0, 0)])
    visited = [[0]*M for _ in range(N)]
    visited[0][0] = 1

    while deq:
        y, x = deq.popleft()

        for dy, dx in zip([0, 1, 0, -1], [1, 0, -1, 0]):
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < M:
                if _graph[ny][nx] == 0 and visited[ny][nx] == 0:
                    deq.append((ny, nx))
                    external.add((ny, nx))
                    visited[ny][nx] = 1

    return list(external)


def isTarget(_y, _x, _graph, _external):
    global N, M

    count = 0
    for dy, dx in zip([0, 1, 0, -1], [1, 0, -1, 0]):
        ny, nx = _y+dy, _x+dx
        if _graph[ny][nx] == 1 or (ny, nx) not in _external:
            count += 1

    return False if count > 2 else True


result = 0
while not isComplete(graph):
    result += 1

    external = getExternal(graph)
    target_list = []

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                continue

            if isTarget(i, j, graph, external):
                target_list.append((i, j))

    for i, j in target_list:
        graph[i][j] = 0

print(result)
