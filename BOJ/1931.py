### Silver 1 ###

# 1차: 220901

'''
회의실 배정
- 그리디 알고리즘
- 정렬
'''


import sys

input = sys.stdin.readline

N = int(input())
meet = []
for _ in range(N):
    meet.append(list(map(int, input().split())))

# meet.sort(key=lambda x: (x[0], x[1]))
meet = sorted(meet, key=lambda x: (x[0]))
meet = sorted(meet, key=lambda x: (x[1]))

answer, end = 0, 0
for s, e in meet:
    if s >= end:
        end = e
        answer += 1

print(answer)
