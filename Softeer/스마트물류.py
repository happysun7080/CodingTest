'''
level: 3/5 - 스마트 물류
'''

import sys

input = sys.stdin.readline
N, K = map(int, input().split())
lane = list(input().strip())

for i in range(N):
    if lane[i] != 'P':
        continue
    for j in range(i-K, i+K+1):
        if j < 0 or j > N-1:
            continue
        if lane[j] == 'H':
            lane[j] = 'X'
            break

print(lane.count('X'))
