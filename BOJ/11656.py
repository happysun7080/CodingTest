### Silver 5 ###

# 1차: 210126
# 2차: 220423

'''
접미사 배열
- 정렬
'''


S = input()
r = []
for i in range(len(S)):
    r.append(S[i:])
r.sort()
for i in r:
    print(i)
