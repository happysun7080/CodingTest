### Silver 4 ###

# 1차: 210128
# 2차: 211121

'''
통계학
- 구현
- 정렬
'''



from collections import Counter
import sys as s

N = int(s.stdin.readline())
M = []
for _ in range(N):
    M.append(int(s.stdin.readline()))
M.sort()

r = []
r.append(round(sum(M)/N))
r.append(M[N//2])
tmp = Counter(M).most_common()
if len(tmp) > 1:
    if tmp[0][1] != tmp[1][1]:
        r.append(tmp[0][0])
    else:
        r.append(tmp[1][0])
else:
    r.append(tmp[0][0])
r.append(M[-1]-M[0])

for i in r:
    print(i)
