### Gold 5 ###

# 1차: 210201
# 2차: 220515

'''
로봇 청소기
- 구현
'''


def count(X):
    rlt = 0
    for x in X:
        rlt += x.count(2)
    return rlt


N, M = map(int, input().split())
r, c, d = map(int, input().split())
K = []
for _ in range(N):
    K.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]  # 왼(0)/아(1)/오(2)/위(3)
dy = [0, 1, 0, -1]
d = abs(d-3)

while True:
    K[r][c] = 2

    for i in range(d+1, d+5):
        if K[r+dy[i % 4]][c+dx[i % 4]] == 0:
            d = i % 4
            r += dy[d]
            c += dx[d]
            break
        elif i == d+4:  # 4방향 모두 0이 아님
            f = True
            while f:  # 0을 만날 때 까지 반대방향으로 계속 탐색
                r += dy[(d+2) % 4]
                c += dx[(d+2) % 4]
                if K[r][c] == 0:
                    break  # 탐색한 칸이 0이면 stop
                elif K[r][c] == 1:
                    print(count(K))
                    exit()

                for j in range(d+1, d+5):  # 탐색한 칸이 0이 아닐 때 그 주위 탐색
                    if K[r+dy[j % 4]][c+dx[j % 4]] == 0:
                        d = j % 4
                        r += dy[d]
                        c += dx[d]
                        f = False
                        break
