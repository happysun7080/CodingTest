### Silver 4 ###

# 1차: 210131
# 2차: 220408

'''
큐
- 자료구조
'''


import sys

input = sys.stdin.readline


def queue(q, o, t=0):
    rt = 0
    if o == 'push':
        q.append(t)
    elif o == 'pop':
        if q:
            rt = q.pop(0)
        else:
            rt = -1
    elif o == 'size':
        rt = len(q)
    elif o == 'empty':
        if q:
            rt = 0
        else:
            rt = 1
    elif o == 'front':
        if q:
            rt = q[0]
        else:
            rt = -1
    else:  # back
        if q:
            rt = q[-1]
        else:
            rt = -1

    if o != 'push':
        print(rt)


Q = []
for _ in range(int(input())):
    O = list(input().split())
    if len(O) == 2:
        queue(Q, O[0], int(O[1]))
    else:
        queue(Q, O[0])
