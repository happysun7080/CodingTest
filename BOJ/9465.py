### Silver 1 ###

# 1차: 220920

'''
스티커
- DP
'''


for _ in range(int(input())):
    n = int(input())
    stickers = []
    for _ in range(2):
        stickers.append(list(map(int, input().split())))
    dp = [[0]*(n+1) for _ in range(2)]
    dp[0][1] = stickers[0][0]
    dp[1][1] = stickers[1][0]

    for i in range(2, n+1):
        for j in range(2):
            if j == 0:
                dp[j][i] = stickers[j][i-1] + \
                    max(dp[j+1][i-1], dp[j][i-2], dp[j+1][i-2])
            else:
                dp[j][i] = stickers[j][i-1] + \
                    max(dp[j-1][i-1], dp[j][i-2], dp[j-1][i-2])

    answer = 0
    for i in range(2):
        answer = max(answer, max(dp[i]))
    print(answer)
