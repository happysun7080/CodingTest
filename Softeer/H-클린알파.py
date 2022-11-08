'''
level: 4/5 - H-클린알파
'''

import sys

input = sys.stdin.readline
P, N = map(int, input().split())
A = list(map(int, input().split()))
DIVISOR = int(1e9 + 7)

answer = 0
for a in A:
    answer = (answer * P + a) % DIVISOR

print(answer)
