### Silver 1 ###

# 1차: 220308

'''
A -> B
- 그리디 알고리즘
- BFS
'''

from collections import deque

A, B = map(int, input().split())

rlt = -1
D = deque()
D.append((A, 1))
while D:
    i, cnt = D.popleft()

    if i == B:
        rlt = cnt
        break

    if i*2 <= B:
        D.append((i*2, cnt + 1))

    if int(str(i) + '1') <= B:
        D.append((int(str(i) + '1'), cnt + 1))

print(rlt)