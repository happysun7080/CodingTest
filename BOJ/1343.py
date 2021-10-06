### Silver 5 ###

# 1차: 210120
# 2차: 211006

'''
폴리노미오
- 그리디 알고리즘
'''


p = list(input())
p += '.'

_X = 0
for i in range(len(p)):
    if p[i] == 'X':
        _X += 1
    else:
        if _X:
            if _X % 2:
                print(-1)
                exit()
            else:
                case = (_X/2) % 2

            for j in range(i-_X, i-2):
                p[j] = 'A'
            for j in range(i-2, i):
                if case:
                    p[j] = 'B'
                else:
                    p[j] = 'A'
            _X = 0

p.pop()
for i in p:
    print(i, end='')
