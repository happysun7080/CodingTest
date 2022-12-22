### Gold 5 ###

# 1차: 221222

'''
적록색약
- DFS/BFS
'''

import sys
sys.setrecursionlimit(10000)


N = int(input())
graph = [[i for i in input()] for _ in range(N)]


def dfs(y, x, element):
    global N, graph
    visited[y][x] = True

    for dy, dx in zip([0, 0, 1, -1], [1, -1, 0, 0]):
        ny, nx = y + dy, x + dx

        if 0 <= ny < N and 0 <= nx < N \
                and graph[ny][nx] in element \
                and not visited[ny][nx]:
            dfs(ny, nx, element)


visited = [[False] * N for _ in range(N)]
not_blind = 0

for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            dfs(y, x, [graph[y][x]])
            not_blind += 1

visited = [[False] * N for _ in range(N)]
blind = 0

for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            dfs(y, x, ['B'] if graph[y][x] == 'B' else ['R', 'G'])
            blind += 1

print(not_blind, blind)
