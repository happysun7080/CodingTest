'''
Q37 플로이드

level: 1.5/3
reference: Baekjoon 11404
'''


import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a][b] = min(graph[a][b], cost)

for i in range(1, n + 1):
    graph[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            graph[i][j] = 0

for i in range(1, n + 1):
    print(" ".join(map(str, graph[i][1:])))
