'''
level: 3/5 - 징검다리
'''


import sys

input = sys.stdin.readline

N = int(input())
stones = list(map(int, input().split()))
result = [1]

for i in range(1, N):
    pre_max = 0
    for j in range(i):
        if stones[i] > stones[j]:
            if pre_max < result[j]:
                pre_max = result[j]

    result.append(pre_max + 1)

print(max(result))
