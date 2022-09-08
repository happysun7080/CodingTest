### Silver 2 ###

# 1차: 220906

'''
가장 긴 증가하는 부분 수열
- DP
'''


N = int(input())
nums = list(map(int, input().split()))
dp = [0 for _ in range(N)]
for i in range(N):
    for j in range(i):
        if nums[i] > nums[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))
