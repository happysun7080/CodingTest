### Silver 5 ###

# 1차: 210128
# 2차: 220404

'''
나이 순 정렬
- 정렬
'''


import sys

M = []
for i in range(int(sys.stdin.readline())):
    M.append(list(sys.stdin.readline().split()))

M.sort(key=lambda x: int(x[0]))
for i in M:
    print(i[0], i[1])
