### DFS/BFS ###

'''
5-11 미로 탈출

level: 1.5/3
'''

from collections import deque

N, M = map(int, input().split())
miro = []
for _ in range(N):
    miro.append(list(map(int, input())))

way = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def bfs(y, x):
    queue = deque()
    queue.append((y, x))

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            new_y = y + way[i][0]
            new_x = x + way[i][1]

            if new_y < 0 or new_y >= N or new_x < 0 or new_x >= M:
                continue

            if miro[new_y][new_x] == 0:
                continue

            if miro[new_y][new_x] == 1:
                miro[new_y][new_x] = miro[y][x] + 1
                queue.append((new_y, new_x))

    return miro[N-1][M-1]


print(bfs(0, 0))
