'''
level: 3/5 - 우물 안 개구리
'''


import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
weights = list(map(int, input().split()))
fams = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    fams[a].append(b)
    fams[b].append(a)

result = 0
for i, weight in enumerate(weights):
    is_best = True
    for fam in fams[i+1]:
        if weights[fam-1] >= weight:
            is_best = False
            break

    if is_best:
        result += 1

print(result)
