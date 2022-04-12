### Silver 4 ###

# 1차: 210131
# 2차: 220412

'''
덱
- 자료구조
'''


from collections import deque
import sys

dq = deque()
for _ in range(int(sys.stdin.readline())):
    O = list(sys.stdin.readline().split())
    if O[0] == 'push_front':
        dq.appendleft(O[1])
    elif O[0] == 'push_back':
        dq.append(O[1])
    elif O[0] == 'pop_front':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif O[0] == 'pop_back':
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif O[0] == 'size':
        print(len(dq))
    elif O[0] == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif O[0] == 'front':
        if dq:
            tmp = dq.popleft()
            print(tmp)
            dq.appendleft(tmp)
        else:
            print(-1)
    else:  # back
        if dq:
            tmp = dq.pop()
            print(tmp)
            dq.append(tmp)
        else:
            print(-1)
