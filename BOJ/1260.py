### Silver 2 ###

# 1차: 221206

'''
DFS와 BFS
- DFS/BFS
'''


from collections import defaultdict, deque

N, M, V = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for value in graph.values():
    value.sort()

dfs_result, bfs_result = [], []


def dfs(current):
    global graph, N, visited

    visited[current] = True
    dfs_result.append(current)

    for node in graph[current]:
        if not visited[node]:
            dfs(node)


def bfs():
    global graph, N, V, visited

    visited[V] = True

    bfs_result.append(V)

    queue = deque()
    for node in graph[V]:
        queue.append(node)

    while queue:
        current = queue.popleft()
        visited[current] = True
        bfs_result.append(current)

        next_nodes = graph[current]
        for node in next_nodes:
            if not visited[node] and node not in queue:
                queue.append(node)


visited = [False for _ in range(N + 1)]
bfs()
visited = [False for _ in range(N + 1)]
dfs(V)
print(" ".join(map(str, dfs_result)))
print(" ".join(map(str, bfs_result)))
