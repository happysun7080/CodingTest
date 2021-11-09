### Silver 4 ###

# 1차: 210127
# 2차: 211109

'''
수 찾기
- 이분 탐색
'''

n = int(input())
N = list(map(int, input().split()))
N.sort()
m = int(input())
M = list(map(int, input().split()))

for _M in M:
    r = 0
    up = n-1
    dn = 0
    while up >= dn:
        md = (up + dn) // 2
        if _M < N[md]:
            up = md-1
        elif _M > N[md]:
            dn = md+1
        else:
            r = 1
            break
    print(r)

