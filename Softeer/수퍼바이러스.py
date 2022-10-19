'''
level: 3/5 - 수퍼바이러스
'''


import sys

input = sys.stdin.readline
K, P, N = map(int, input().split())
DIVISOR = int(1e9 + 7)

print(K * pow(P, N*10, DIVISOR) % DIVISOR)
