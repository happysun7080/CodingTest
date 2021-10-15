### Silver 3 ###

# 1차: 210204
# 2차: 211015

'''
1로 만들기
- DP
'''


N = int(input())

D = {1: 0, 2: 1, 3: 1}
for i in range(4, N+1):
    a = D[i//3] + 1 if not i % 3 else 9999999
    b = D[i//2] + 1 if not i % 2 else 9999999
    c = D[i-1] + 1
    D[i] = min(a, b, c)
print(D[N])

