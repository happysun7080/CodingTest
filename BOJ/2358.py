### Silver 5 ###

# 1차: 210118
# 2차: 211125

'''
평행선  
- 자료구조
- 정렬
'''

from operator import itemgetter

n = int(input())

r = 0
k = []

for i in range(n):
    tmp = list(map(int, input().split()))
    k.append(tmp)

for i in k:
    if k[:][0].count(i[0]) >= 2:
        r += 1
    if k[:][1].count(i[1]) >= 2:
        r += 1

print(r)
