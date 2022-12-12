'''
10-4 서로소 집합을 활용한 사이클 판별

level: 1/3
'''


def find_parent(parent, x):
    '''
    특정 원소가 속한 집합 찾기
    '''
    # 루트 노드가 아니라면, 루트 노드를 찾을 때 까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent, a, b):
    '''
    두 원소가 속한 집합 합치기
    '''
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선(union 연산)의 개수 입력
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

cycle = False

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())

    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다")

# 3 3
# 1 2
# 1 3
# 2 3
