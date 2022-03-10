### Implementation ###

'''
4-4 게임 개발

level: 2/3
'''

N, M = map(int, input().split())
A, B, D = map(int, input().split())
MAP = []
for i in range(N): MAP.append(list(map(int, input().split())))

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

visited = [(A, B)]
cnt = 0
rlt = 1

while True:
    
    next_A = A + direction[D][0]
    next_B = B + direction[D][1]

    if 0 <= next_A < N and 0 <= next_B < M and MAP[next_A][next_B] == 0 and (next_A, next_B) not in visited:
        A = next_A
        B = next_B

        if (A, B) not in visited:
            rlt += 1
            visited.append((A, B))

        cnt = 0
    else:
        cnt += 1

        back_A = A + direction[(D-2)%4][0]
        back_B = B + direction[(D-2)%4][1]

        if cnt == 4:
            if 0 <= back_A < N and 0 <= back_B < M and MAP[back_A][back_B] == 0:
                A = back_A
                B = back_B
                cnt = 0
            else:
                break
        else:
            D = (D - 1) % 4

print(rlt)