### Silver 3 ###

# 1차: 210127
# 2차: 220303

'''
나무 자르기
- 이분 탐색
'''

import sys
import time
start = time.time()

N,M = map(int,sys.stdin.readline().split())
T = list(map(int,sys.stdin.readline().split()))

up = max(T)
dn = 0
while up >= dn:
    r = (up + dn) // 2
    _M = 0
    for t in T:
        if r < t: _M += t - r
        if _M > M: break
    if _M >= M: dn = r+1
    else: up = r-1

print(up)


print("time :", time.time() - start)
