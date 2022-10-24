'''
level: 2/5 - 지도 자동 구축
'''

import sys

input = sys.stdin.readline

N = int(input())

points = []
cur = 3
for i in range(N):
    points.append(cur**2)
    cur = cur + cur-1

print(points[-1])
