### Silver 1 ###

# 1차: 220903

'''
2xn 타일링
- DP
'''


n = int(input())

if n == 1:
    print(1)
    exit()

dp = [0 for _ in range(n+1)]
dp[1], dp[2] = 1, 2
for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])
