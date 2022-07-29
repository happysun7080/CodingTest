### Gold 3 ###

# 1차: 220729

'''
행렬 곱셈 순서
- DP
'''

import sys

input = sys.stdin.readline

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

dp = [[0 for _ in range(len(matrix))]
      for _ in range(len(matrix))]

for i in range(1, len(matrix)):
    for j in range(0, len(matrix) - i):
        k = j + i

        cur = []
        for m in range(j, k):
            cur.append(
                dp[j][m] +
                dp[m+1][k] +
                matrix[j][0] * matrix[m][1] * matrix[k][1])
        dp[j][k] = min(cur)

print(dp[0][-1])
