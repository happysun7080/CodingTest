### Silver 2 ###

# 1차: 220906

'''
1, 2, 3 더하기 3
- DP
'''


dp = [0, 1, 2, 4]
for i in range(4, 1000001):
    dp.append((dp[i-1]+dp[i-2]+dp[i-3]) % 1000000009)

for _ in range(int(input())):
    print(dp[int(input())])
