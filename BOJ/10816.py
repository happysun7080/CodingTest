### Silver 4 ###

# 1차: 210131
# 2차: 220406

'''
숫자 카드 2
- 정렬
'''


from collections import Counter
import sys

N = int(sys.stdin.readline())
_N = Counter(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
_M = list(map(int, sys.stdin.readline().split()))

for m in _M:
    print(_N[m], end=' ')
