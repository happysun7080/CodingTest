### Gold 3 ###

# 1차: 221125

'''
소형기관차
- DP
'''


N = int(input())
trains = list(map(int, input().split()))
M = int(input())

S = [0]
for train in trains:
    S.append(S[-1] + train)

dp = [[0] * (N+1) for _ in range(4)]
for i in range(1, 4):
    for j in range(i*M, N+1):
        if i == 1:
            dp[i][j] = max(dp[i][j-1], S[j] - S[j-M])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-M] + S[j] - S[j-M])

print(dp[-1][-1])
