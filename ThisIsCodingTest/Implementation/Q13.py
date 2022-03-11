### Greedy ###

'''
Q13 치킨 배달

level: 2/3
reference: Baekjoon 15686
'''


import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
city = []
for _ in range(N): city.append(list(map(int, input().split())))

house = []
chick = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i+1, j+1))
        elif city[i][j] == 2:
            chick.append((i+1, j+1))

close = combinations(chick, M)

dist = []

for c in close:
    dsum = 0
    for h in house:
        tdist = 100000
        for cl in c:
            tmp = abs(h[0]-cl[0]) + abs(h[1]-cl[1])
            if tmp < tdist:
                tdist = tmp
        dsum += tdist
    dist.append(dsum)

print(min(dist))


