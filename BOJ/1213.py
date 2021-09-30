### Silver 4 ###

# 1차: 210120
# 2차: 210930

'''
팰린드롬 만들기
- 구현
- 문자열
'''


N = list(input())
N.sort()

ans = []
k = []
v = []
idx = -1

for i in N:
    if i in k:
        continue
    k.append(i)
    v.append(N.count(i))

ln = len(k)

for j in range(ln):
    ans += (v[j]//2)*k[j]
    if v[j] % 2:
        if idx + 1:
            print("I'm Sorry Hansoo")
            exit()
        else:
            idx = j

if idx + 1:
    ans += k[idx]

for j in range(ln-1, -1, -1):
    ans += (v[j]//2)*k[j]

for i in ans:
    print(i, end='')
