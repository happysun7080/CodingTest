'''
level: 2/5 - 전광판
'''

import sys
input = sys.stdin.readline

segments = {
    0: [1, 1, 1, 0, 1, 1, 1],
    1: [0, 0, 1, 0, 0, 1, 0],
    2: [1, 0, 1, 1, 1, 0, 1],
    3: [1, 0, 1, 1, 0, 1, 1],
    4: [0, 1, 1, 1, 0, 1, 0],
    5: [1, 1, 0, 1, 0, 1, 1],
    6: [1, 1, 0, 1, 1, 1, 1],
    7: [1, 1, 1, 0, 0, 1, 0],
    8: [1, 1, 1, 1, 1, 1, 1],
    9: [1, 1, 1, 1, 0, 1, 1],
}


def diff(a, b):
    count = 0

    for _a, _b in zip(a, b):
        if _a != _b:
            count += 1

    return count


for _ in range(int(input())):
    A, B = map(list, input().split())
    result = 0

    while len(A) != len(B):
        if len(A) < len(B):
            current = B.pop(0)
        else:
            current = A.pop(0)
        
        result += segments[int(current)].count(1)

    for a, b in zip(A, B):
        if a != b:
            result += diff(segments[int(a)], segments[int(b)])
    
    print(result)
