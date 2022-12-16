### Gold 1 ###

# 1차: 221216

'''
최종 순위
- 그래프
- 위상 정렬
'''


from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    teams = list(map(int, input().split()))
    m = int(input())
    changes = [list(map(int, input().split())) for _ in range(m)]

    # 모든 노드에 대한 진입 차수는 0으로 초기화
    indegree = [0] * (n + 1)
    # 각 노드에 연결된 간선 정보를 담기 위한 인접 행렬 초기화
    graph = [[False] * (n + 1) for _ in range(n + 1)]

    # 방향 그래프의 간선 정보 초기화
    for i in range(n):
        for j in range(i + 1, n):
            graph[teams[i]][teams[j]] = True
            indegree[teams[j]] += 1

    # 올해 변경된 순위 정보
    for a, b in changes:
        # 간선의 방향 뒤집기
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    # 위상 정렬
    result = []
    queue = deque()

    # 처음 시작할 때는 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    cycle = False # 그래프 내 사이클이 존재하는지 여부
    certain = True # 위상 정렬 결과가 오직 하나인지의 여부

    # 정확히 노드의 개수 만큼 반복
    for _ in range(n):

        # 큐가 비어있다면 사이클이 발생했다는 의미
        if not queue:
            cycle = True
            break
            
        # 큐의 원소가 2개 이상이라면 가능한 정렬 결과가 여러 개라는 의미
        if len(queue) > 1:
            certain = False
            break

        current = queue.popleft()
        result.append(current)

        # 해당 원소와 연결된 노드들의 진입 차수에서 1 빼기
        for j in range(1, n + 1):
            if graph[current][j]:
                indegree[j] -= 1
            
                # 새롭게 진입 차수가 0이 되는 노드들을 큐에 삽입
                if indegree[j] == 0:
                    queue.append(j)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        print(*result)
    print()