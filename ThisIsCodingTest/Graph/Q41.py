### Graph ###

'''
Q41 여행 계획

level: 2/3
reference: 핵심 유형
'''


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
plans = list(map(int, input().split()))
parent = list(range(N + 1))
answer = "YES"

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            union_parent(parent, i + 1, j + 1)

for i in range(M - 1):
    if find_parent(parent, plans[i]) != find_parent(parent, plans[i + 1]):
        answer = "NO"

print(answer)

