### Silver 1 ###

# 1차: 221209

'''
케빈 베이컨의 6단계 법칙
- 그래프
- 플로이드-워셜
'''


N, M = map(int, input().split())
INF = int(1e8)
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b], graph[b][a] = 1, 1

for i in range(N):
    graph[i][i] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = dict()
for i in range(1, N + 1):
    result[i] = sum(graph[i][1:])

result = sorted(result.items(), key=lambda x: (x[1], x[0]))
print(result[0][0])
