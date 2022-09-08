### Gold 4 ###

# 1차: 220908

'''
연구소
- DFS/BFS
'''


N, M = map(int, input().split())
lab = []
answer = 0
lab_wall = [[0]*M for _ in range(N)]
for _ in range(N):
    lab.append(list(map(int, input().split())))


def virus(y, x):
    for dy, dx in zip([0, 0, 1, -1], [1, -1, 0, 0]):
        _y, _x = y + dy, x + dx
        if 0 <= _y < N and 0 <= _x < M:
            if lab_wall[_y][_x] == 0:
                lab_wall[_y][_x] = 2
                virus(_y, _x)


def getScore():
    score = 0
    for row in lab_wall:
        for elem in row:
            if elem == 0:
                score += 1
    return score


def dfs(count):
    global answer

    if count == 3:
        for i in range(N):
            for j in range(M):
                lab_wall[i][j] = lab[i][j]
        for i in range(N):
            for j in range(M):
                if lab_wall[i][j] == 2:
                    virus(i, j)
        answer = max(answer, getScore())
        return

    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1
                count += 1
                dfs(count)
                lab[i][j] = 0
                count -= 1


dfs(0)
print(answer)
