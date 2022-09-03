### Silver 1 ###

# 1차: 220903

'''
기타리스트
- DP
'''


N, S, M = map(int, input().split())
d = list(map(int, input().split()))

dp = [[0] * (M+1) for _ in range(N+1)]
dp[0][S] = 1

for i in range(N):
    for j in range(M+1):
        if dp[i][j] == 1:
            if j+d[i] <= M:
                dp[i+1][j+d[i]] = 1
            if j-d[i] >= 0:
                dp[i+1][j-d[i]] = 1

answer = -1
for i in range(M, -1, -1):
    if dp[N][i] == 1:
        answer = i
        break

print(answer)
