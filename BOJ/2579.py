### Silver 3 ###

# 1차: 220808

'''
계단 오르기
- DP
'''

import sys

input = sys.stdin.readline

N = int(input())
stairs = []
for _ in range(N):
    stairs.append(int(input()))

dp = [[0, 0], [0, 0]]
for i, stair in enumerate(stairs):
    a = max(dp[i]) + stair
    b = dp[i+1][0] + stair
    dp.append([a, b])

print(max(dp[-1]))
