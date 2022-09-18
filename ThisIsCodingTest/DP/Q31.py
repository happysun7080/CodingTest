'''
Q31 금광

level: 1.5/3
reference: Flipkart 인터뷰
'''

for _ in range(int(input())):
    n, m = map(int, input().split())
    array_list = list(map(int, input().split()))
    array = []
    for i in range(0, n*m, m):
        array.append(array_list[i:i+m])

    dp = [[0]*n for _ in range(m)]
    dp[0] = [x[0] for x in array]
    for i in range(1, m):
        for j in range(n):
            if j == 0:
                dp[i][j] = array[j][i] + max(dp[i-1][j], dp[i-1][j+1])
            elif j == n-1:
                dp[i][j] = array[j][i] + max(dp[i-1][j-1], dp[i-1][j])
            else:
                dp[i][j] = array[j][i] + \
                    max(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])

    print(max(dp[-1]))
