### Silver 3 ###

# 1차: 220808

'''
N과 M (2)
- 백트래킹
'''

from itertools import combinations

N, M = map(int, input().split())

arr = [i+1 for i in range(N)]

for p in list(combinations(arr, M)):
    print(*list(p))
