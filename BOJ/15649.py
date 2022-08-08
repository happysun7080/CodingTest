### Silver 3 ###

# 1차: 220808

'''
N과 M (1)
- 백트래킹
'''

from itertools import permutations

N, M = map(int, input().split())

arr = [i+1 for i in range(N)]

for p in list(permutations(arr, M)):
    print(*list(p))
