### Graph ###

'''
Q44 행성 터널

level: 2/3
reference: Baekjoon 2887
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


N = int(input())
points = [map(int, input().split()) for _ in range(N)]
parent = list(range(N + 1))

x, y, z = [], [], []
for i, (_x, _y, _z) in enumerate(points):
    x.append((_x, i + 1))
    y.append((_y, i + 1))
    z.append((_z, i + 1))

x.sort()
y.sort()
z.sort()

edges = []
for i in range(N - 1):
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)