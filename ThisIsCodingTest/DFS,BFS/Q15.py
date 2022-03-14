### Greedy ###

'''
Q15 특정 거리의 도시 찾기

level: 1.5/3
reference: Baekjoon 18352
'''

import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
road = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    road[a].append(b)

dist = [-1] * (N+1)
dist[X] = 0

deq = deque([X])

while deq:
    cur = deq.popleft()

    for r in road[cur]:
        if dist[r] == -1:
            dist[r] = dist[cur] + 1
            deq.append(r)

flag = False
for i in range(1, N+1):
    if dist[i] == K:
        print(i)
        flag = True

if not flag:
    print(-1)
