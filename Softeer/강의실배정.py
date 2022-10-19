'''
level: 3/5 - 강의실 배정
'''


import sys
import heapq

input = sys.stdin.readline
N = int(input())
classes = []
for _ in range(N):
    s, e = map(int, input().split())
    heapq.heappush(classes, (e, s))

result, end = 0, 0
while classes:
    s, e = heapq.heappop(classes)
    if end <= e:
        end = s
        result += 1

print(result)
