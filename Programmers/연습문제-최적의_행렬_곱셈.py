### level 3 ###

# 1차: 220719
# 2차: 220729

'''
연습문제 - 최적의 행렬 곱셈 (12942)
'''


def solution(matrix_sizes):
    dp = [[0 for _ in range(len(matrix_sizes))]
          for _ in range(len(matrix_sizes))]

    for i in range(1, len(matrix_sizes)):
        for j in range(0, len(matrix_sizes) - i):
            k = j + i

            cur = []
            for m in range(j, k):
                cur.append(
                    dp[j][m] +
                    dp[m+1][k] +
                    matrix_sizes[j][0] * matrix_sizes[m][1] * matrix_sizes[k][1])
            dp[j][k] = min(cur)

    return dp[0][-1]


# print(solution([[5, 3], [3, 10], [10, 6]]))
