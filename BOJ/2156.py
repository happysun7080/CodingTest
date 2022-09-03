### Silver 1 ###

# 1차: 220903

'''
포도주 시식
- DP
'''


import sys

input = sys.stdin.readline

n = int(input())
wines = [0]
for _ in range(n):
    wines.append(int(input()))

dp = [0]
dp.append(wines[1])
if n > 1:
    dp.append(wines[2]+wines[1])

for i in range(3, n+1):
    dp.append(max(dp[i-1], wines[i]+dp[i-2], wines[i]+wines[i-1]+dp[i-3]))

print(dp[-1])
