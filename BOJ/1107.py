### Gold 5 ###

# 1차: 210303
# 2차: 210926

'''
리모컨
- BruteForce
'''


import sys
input = sys.stdin.readline


def f(x):
    X = list(str(x))
    for _x in X:
        if _x in M:
            return False
    return True


N = int(input())
_M = int(input())
M = list(input().strip())

r = abs(N-100)
for i in range(1000001):
    if f(i):
        r = min(r, abs(i-N)+len(str(i)))

print(r)
