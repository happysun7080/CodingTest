### Silver 4 ###

# 1차: 220831

'''
바이러스
- 그래프
- DFS/BFS
'''


N = int(input())
E = int(input())

graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(E):
    a, b = map(int, input().split())
    a, b = min(a, b), max(a, b)
    graph[a][b] = 1
    graph[b][a] = 1


def dfs(y, x):

    for i, _x in enumerate(graph[y]):
        if _x == 1:
            graph[i][i] = -1
            graph[i][y] = 2
            graph[y][i] = 2
            dfs(i, x)


dfs(1, 1)

count = 0 if graph[1][1] != -1 else -1
for g in graph:
    count += g.count(-1)

print(count)
