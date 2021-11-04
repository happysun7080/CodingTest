### Silver 3 ###

# 1차: 210127
# 2차: 211105

'''
랜선 자르기
- 이분 탐색
'''

K, N = map(int, input().split())
L = []
for _ in range(K):
    L.append(int(input()))

up = max(L)
dn = 1
while up >= dn:
    c = 0
    m = (up+dn)//2
    for i in L:
        c += i // m
    if c < N:
        up = m-1
    else:
        dn = m+1
print(up)
