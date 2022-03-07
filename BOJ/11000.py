### Gold 5 ###

# 1차: 220308

'''
강의실 배정
- 그리디 알고리즘
'''

import sys
import heapq

input = sys.stdin.readline

c = []
room = []

N = int(input())

for _ in range(N):
    c.append(list(map(int, input().split())))
c.sort(key=lambda x : x[0])

heapq.heappush(room, c[0][1])

for i in range(1, N):
    if c[i][0] < room[0]:
        heapq.heappush(room, c[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, c[i][1])

print(len(room))