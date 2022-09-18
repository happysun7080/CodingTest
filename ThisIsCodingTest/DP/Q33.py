'''
Q33 퇴사

level: 2/3
reference: 삼성전자 SW 역량테스트 (Baekjoon 14501)
'''

N = int(input())
T = [0 for _ in range(N)]
P = [0 for _ in range(N)]
for i in range(N):
    T[i], P[i] = map(int, input().split())

dp = [0 for _ in range(N+1)]
for i in range(N-1, -1, -1):
    if T[i]+i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], P[i]+dp[i+T[i]])

print(dp[0])
