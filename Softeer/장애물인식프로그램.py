'''
level: 2/5 - 장애물 인식 프로그램
'''


import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
graph = [list(map(int, list(input().strip()))) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
count_list = []

for i in range(N):
    for j in range(N):
        if graph[i][j] and not visited[i][j]:
            deq = deque([(i, j)])
            count = 1
            visited[i][j] = 1

            while deq:
                y, x = deq.popleft()
                for dy, dx in zip([0, 1, 0, -1], [1, 0, -1, 0]):
                    ny, nx = y+dy, x+dx
                    if 0 <= ny < N and 0 <= nx < N:
                        if graph[ny][nx] and not visited[ny][nx]:
                            count += 1
                            visited[ny][nx] = 1
                            deq.append((ny, nx))

            count_list.append(count)

print(len(count_list))
print(*sorted(count_list), sep='\n')
