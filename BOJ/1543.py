### Silver 4 ###

# 1차: 210126
# 2차: 211103

'''
문서 검색
- 문자열
- 그리디 알고리즘
- BruteForce
'''


D = list(input())
W = list(input())
ct = r = 0
while ct <= len(D)-len(W):
    if D[ct:ct+len(W)] == W:
        r += 1
        ct += len(W)
    else:
        ct += 1
print(r)
