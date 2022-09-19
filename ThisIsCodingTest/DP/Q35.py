'''
Q35 못생긴 수

level: 1.5/3
reference: Google 인터뷰
'''

n = int(input())

dp = [0 for _ in range(n)]
dp[0] = 1

i2 = i3 = i5 = 0
n2, n3, n5 = 2, 3, 5

for j in range(1, n):
    dp[j] = min(n2, n3, n5)

    if dp[j] == n2:
        i2 += 1
        n2 = dp[i2] * 2
    if dp[j] == n3:
        i3 += 1
        n3 = dp[i3] * 3
    if dp[j] == n5:
        i5 += 1
        n5 = dp[i5] * 5

print(dp[n-1])
