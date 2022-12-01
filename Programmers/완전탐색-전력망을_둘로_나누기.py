### level 2 ###

# 1차: 221129

'''
완전탐색 - 전력망을 둘로 나누기 (86971)
'''

from collections import defaultdict, deque


def solution(n, wires):
    results = []

    for i in range(len(wires)):
        graph = makeGraph(wires[:i] + wires[i+1:])
        visited = [False for _ in range(n + 1)]
        counts = []

        for i in range(1, n + 1):
            if visited[i]:
                continue

            counts.append(bfs(graph, i, visited))

        counts.sort()
        results.append(counts[-1] - counts[-2])

    return min(results)


def bfs(graph, current, visited):
    queue = deque([current])
    visited[current] = True
    count = 0

    while queue:
        next_ = queue.popleft()
        count += 1

        for i in graph[next_]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    return count


def makeGraph(wires):
    graph = defaultdict(list)

    for start, end in wires:
        graph[start].append(end)
        graph[end].append(start)

    return graph


print(solution(9, [[1, 3], [2, 3], [3, 4],
                   [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))
