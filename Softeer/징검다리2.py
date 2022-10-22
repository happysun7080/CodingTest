'''
level: 4/5 - 징검다리2
'''


import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
stones = list(map(int, input().split()))


def calc(_stones):
    pre = [_stones[0]]
    result = [0 for _ in range(N)]
    result[0] = 1

    for i in range(1, N):
        if _stones[i] > pre[-1]:
            pre.append(_stones[i])
            result[i] = len(pre)
        else:
            idx = bisect_left(pre, _stones[i])
            pre[idx] = _stones[i]
            result[i] = idx + 1

    return result


result_up = calc(stones)
result_down = calc(stones[::-1])
result = [up+down-1 for up, down in zip(result_up, result_down[::-1])]
print(max(result))
