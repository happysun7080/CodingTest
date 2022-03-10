### Greedy ###

'''
Q04 만들 수 없는 금액

level: 1/3
reference: K대회 기출
'''

from itertools import combinations

N = int(input())
C = list(map(int, input().split()))

S = set()

for i in range(N):
    tmp = list(combinations(C, i+1))
    for j in tmp:
        S.add(sum(j))

S = sorted(S)

idx = 1
for i in S:
    if idx != i:
        print(idx)
        break
    else:
        idx += 1
