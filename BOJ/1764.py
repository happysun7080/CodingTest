### Silver 4 ###

# 1차: 210220
# 2차: 211106

'''
듣보잡
- 정렬
'''

def stoi(s):
    r = ''
    for i in s:
        r += str(ord(i)-87)
    return r


def itos(i):
    r = ''
    for k in range(0, len(i), 2):
        r += chr(87+int(i[k])*10+int(i[k+1]))
    return r


_N, _M = map(int, input().split())
N = []
M = []
R = []
_R = []
for _ in range(_N):
    N.append(stoi(input()))
for _ in range(_M):
    M.append(stoi(input()))
N.sort()

for m in M:
    up = _N-1
    dn = 0
    while up >= dn:
        md = (up + dn) // 2
        if N[md] > m:
            up = md-1
        elif N[md] < m:
            dn = md+1
        else:
            R.append(m)
            break

for r in R:
    _R.append(itos(r))
print(len(_R))
_R.sort()
for r in _R:
    print(r)
