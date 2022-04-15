### Silver 5 ###

# 1차: 210131
# 2차: 220415

'''
수 정렬하기 3
- 정렬
'''


import sys

K = [0 for _ in range(10001)]
for _ in range(int(sys.stdin.readline())):
    K[int(sys.stdin.readline())] += 1
for i in range(10001):
    if K[i]:
        for j in range(K[i]):
            print(i)
