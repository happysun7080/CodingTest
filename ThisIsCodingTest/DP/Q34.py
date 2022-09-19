'''
Q34 병사 배치하기

level: 1.5/3
reference: Baekjoon 18353
'''


N = int(input())
K = list(map(int, input().split()))
d = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if K[j] > K[i]:
            d[i] = max(d[i], d[j]+1)

print(N-max(d))
