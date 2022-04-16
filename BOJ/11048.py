### Gold 5 ###

# 1차: 210203
# 2차: 220416

'''
이동하기
- DP
'''


mz = []
N, M = map(int, input().split())
for _ in range(N):
    mz.append(list(map(int, input().split())))

for i in range(N-1, -1, -1):
    for j in range(M-1, -1, -1):
        if i == N-1 and j == M-1:
            continue
        if i == N-1:
            tmp = mz[i][j+1]
        elif j == M-1:
            tmp = mz[i+1][j]
        else:
            tmp = max(mz[i][j+1], mz[i+1][j], mz[i+1][j+1])
        mz[i][j] += tmp

print(mz[0][0])
