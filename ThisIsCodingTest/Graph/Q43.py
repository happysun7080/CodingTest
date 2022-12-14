### Graph ###

'''
Q43 어두운 길

level: 2/3
reference: University of Ulm Local Contest
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
edges = [list(map(int, input().split())) for _ in range(M)]
parent = list(range(N + 1))
result = 0

edges.sort()
total = 0

for edge in edges:
    a, b, cost = edge
    total += cost

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(total - result)

