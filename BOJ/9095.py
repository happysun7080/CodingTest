### Silver 3 ###

# 1차: 220808

'''
1, 2, 3 더하기
- DP
'''


T = int(input())

dp = [1, 2, 4]
for i in range(3, 11):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])

for _ in range(T):
    print(dp[int(input()) - 1])
