### level 2 ###

# 1차: 220903

'''
연습문제 - 2xn 타일링(12900)
'''


def solution(n):
    dp = [0 for _ in range(n+1)]
    dp[1], dp[2] = 1, 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

    return dp[n]
