'''
10-8 도시 결성 계획

level: 2/3
reference: Baekjoon 1647
'''


import sys
input = sys.stdin.readline


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
edges = []
for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

parent = list(range(N + 1))
result = []

edges.sort()

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result.append(cost)

print(sum(result[:-1]))