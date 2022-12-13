'''
level: 3/5 - 사물인식 최소 면적 산출 프로그램
'''


import sys
input = sys.stdin.readline
INF = int(1e9)

N, K = map(int, input().split())
points = [[] for _ in range(K + 1)]
for _ in range(N):
    x, y, k = map(int, input().split())
    points[k].append((x, y))

answer = INF


def dfs(x1, y1, x2, y2, depth, current):
    global answer, K

    if depth == K + 1:
        if answer > current:
            answer = current
        return

    for point in points[depth]:
        x_1, y_1, x_2, y_2 = x1, y1, x2, y2
        
        if point[0] < x1:
            x_1 = point[0]
        if point[0] > x2:
            x_2 = point[0]
        if point[1] < y1:
            y_1 = point[1]
        if point[1] > y2:
            y_2 = point[1]

        temp = abs(x_2 - x_1) * abs(y_2 - y_1)

        if temp < answer:
            dfs(x_1, y_1, x_2, y_2, depth + 1, temp)


for point in points[1]:
    dfs(point[0], point[1], point[0], point[1], 2, 0)

print(answer)
