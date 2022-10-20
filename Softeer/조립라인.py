'''
level: 3/5 - 조립라인
'''


import sys

input = sys.stdin.readline
N = int(input())
works = [list(map(int, input().split())) for _ in range(N-1)]
works.append(list(map(int, input().split())))

result = []
for i in range(N-1):
    a = works[i+1][0] + min(works[i][0], works[i][1] + works[i][3])
    b = works[i+1][1] + min(works[i][1], works[i][0] + works[i][2])
    works[i+1][0], works[i+1][1] = a, b

print(min(works[-1]))
