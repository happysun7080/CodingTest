'''
10-6 위상 정렬

level: 1/3
'''


from collections import deque

# 노드의 개수와 간선의 개수 입력
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # 정점 A에서 B로 이동 가능

    # 진입 차수를 1 증가
    indegree[b] += 1


def topology_sort():
    '''
    위상 정렬 함수
    '''
    result = []
    queue = deque()

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        current = queue.popleft()
        result.append(current)

        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[current]:
            indegree[i] -= 1

            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                queue.append(i)

    # 위상 정렬 결과 출력
    for i in result:
        print(i, end=' ')


topology_sort()
