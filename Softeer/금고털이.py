'''
level: 2/5 - 금고털이
'''


import sys

input = sys.stdin.readline

W, N = map(int, input().split())
gems = []
for _ in range(N):
    gems.append(list(map(int, input().split())))

gems = sorted(gems, key=lambda x: x[-1], reverse=True)

result = 0
for weight, price in gems:
    if W > weight:
        W -= weight
        result += weight * price
    else:
        result += W * price
        break

print(result)
