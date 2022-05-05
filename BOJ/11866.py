### Silver 4 ###

# 1차: 210131
# 2차: 220505

'''
요세푸스 문제 0
- 구현
- 자료구조
'''


N, K = map(int, input().split())
c = 1
i = 1
r = []

N = list(range(1, N+1))

while len(N) >= 1:
    if c % K == 0:
        r.append(N[i-1])
        N.pop(i-1)
        i -= 1
        c = 0
    c += 1
    i += 1
    if i-1 >= len(N):
        i = 1

print("<", ", ".join(map(str, r))[:], ">", sep='')
