### Gold 5 ###

# 1차: 220908

'''
감시 피하기
- 백트래킹
- BruteForce
- DFS/BFS
'''


from itertools import combinations


N = int(input())
graph = []
teachers, spaces = [], []
for i in range(N):
    graph.append(list(map(str, input().split())))
    for j in range(N):
        if graph[i][j] == 'T':
            teachers.append((i, j))
        if graph[i][j] == 'X':
            spaces.append((i, j))


def watch(y, x, direction):
    if direction == 'left':
        while x >= 0:
            if graph[y][x] == 'S':
                return True
            if graph[y][x] == 'O':
                return False
            x -= 1
    if direction == 'right':
        while x < N:
            if graph[y][x] == 'S':
                return True
            if graph[y][x] == 'O':
                return False
            x += 1
    if direction == 'down':
        while y < N:
            if graph[y][x] == 'S':
                return True
            if graph[y][x] == 'O':
                return False
            y += 1
    if direction == 'up':
        while y >= 0:
            if graph[y][x] == 'S':
                return True
            if graph[y][x] == 'O':
                return False
            y -= 1

    return False


def check():
    for y, x in teachers:
        for d in ['left', 'right', 'down', 'up']:
            if watch(y, x, d):
                return True

    return False


find = False
for comb in combinations(spaces, 3):
    for y, x in comb:
        graph[y][x] = 'O'

    if not check():
        find = True
        break

    for y, x in comb:
        graph[y][x] = 'X'

print('YES' if find else 'NO')
