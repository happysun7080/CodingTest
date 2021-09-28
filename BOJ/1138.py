### Silver 2 ###

# 1차: 210122
# 2차: 210928

'''
한 줄로 서기
- 구현
'''


import sys

N = int(input())
k = list(map(int, sys.stdin.readline().split()))
r = [0 for _ in range(N)]

for i in range(N):
    ct = 0
    for j in range(N):
        if r[j] == 0:
            if ct == k[i]:
                r[j] = i + 1
                break
            else: ct += 1

for i in r: print(i, end=' ')
