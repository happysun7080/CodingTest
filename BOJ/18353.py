### Silver 2 ###

# 1차: 210727
# 2차: 220919

'''
병사 배치하기
- DP
'''


N = int(input())
K = list(map(int, input().split()))
d = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if K[j] > K[i]:
            d[i] = max(d[i], d[j]+1)

print(N-max(d))
