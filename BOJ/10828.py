### Silver 4 ###

# 1차: 210131
# 2차: 220407

'''
스택
- 자료구조
'''


import sys

input = sys.stdin.readline


def stack(s, o, t=0):
    rt = 0
    if o == 'push':
        s.append(t)
    elif o == 'pop':
        if s:
            rt = s.pop()
        else:
            rt = -1
    elif o == 'size':
        rt = len(s)
    elif o == 'empty':
        if s:
            rt = 0
        else:
            rt = 1
    else:  # top
        if s:
            rt = s[-1]
        else:
            rt = -1

    if o != 'push':
        print(rt)


S = []
for _ in range(int(input())):
    O = list(input().split())
    if len(O) == 2:
        stack(S, O[0], int(O[1]))
    else:
        stack(S, O[0])
