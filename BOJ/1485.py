### Silver 4 ###

# 1차: 210122
# 2차: 211102

'''
정사각형
- 기하학
'''

T = int(input())

for _ in range(T):
    k, l = [], []
    for _ in range(4):
        X, Y = map(int, input().split())
        k.append([X, Y])

    k.sort()
    for i in range(3):
        for j in range(i+1, 4):
            l.append((k[i % 4][0] - k[j % 4][0])**2 +
                     (k[i % 4][1] - k[j % 4][1])**2)

    l.sort()
    if l.count(l[0]) == 4 and l.count(l[5]) == 2:
        r = 1
    else:
        r = 0

    print(r)
