### Silver 3 ###

# 1차: 210127
# 2차: 211108

'''
스택 수열
- 자료구조
'''


N = int(input())
P = []
r = []
ct = f = 0
for _ in range(N):
    i = int(input())
    while ct < i:
        ct += 1
        P.append(ct)
        r.append('+')

    if P[-1] == i:
        P.pop()
        r.append('-')
    else:
        f = 1

if f:
    print('NO')
else:
    for i in r:
        print(i)
 
