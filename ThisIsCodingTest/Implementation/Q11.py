### Greedy ###

'''
Q11 뱀

level: 2/3
reference: 삼성전자 SW 역량테스트 (Baekjoon 3190)
'''


from collections import deque

N = int(input())
K = int(input())

board = [[0] * N for _ in range(N)]
for _ in range(K): 
    _y, _x = map(int, input().split())
    board[_y-1][_x-1] = 1
    
L = int(input())
turn = []
for _ in range(L): turn.append(tuple(map(str, input().split())))

snake = deque(); snake.append([0, 0])
cur = [0, 0]
count = 0
way = [[0, 1], [1, 0], [0, -1], [-1, 0]]
fway = 0
fturn = 0

while True:

    if turn[fturn][0] == str(count):
        if turn[fturn][1] == 'D':
            fway = (fway + 1) % 4
        else:
            fway = (fway - 1) % 4
        
        if fturn+1 < L: fturn += 1
    
    count += 1

    y = cur[0] + way[fway][0]
    x = cur[1] + way[fway][1]
    
    # print(count, snake)

    if [y, x] in snake: break

    if 0 <= y < N and 0 <= x < N:
        if board[y][x] != 1:
            snake.popleft()
        else:
            board[y][x] = 0

        snake.append([y, x])

    else: break

    cur[0] = y
    cur[1] = x

print(count)

