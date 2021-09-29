### Silver 5 ###

# 1차: 210119
# 2차: 210929

'''
요세푸스 문제
- 자료 구조
- queue
'''


N, K = map(int, input().split())
c = 1
i = 1
r = []

N = list(range(1,N+1))

while len(N) >= 1:
    if c % K == 0:
        r.append(N[i-1])
        N.pop(i-1)
        i -= 1
        c = 0
    c += 1
    i += 1
    if i-1 >= len(N): i = 1

print("<", ", ".join(map(str, r))[:], ">", sep='')
