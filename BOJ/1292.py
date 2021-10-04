### Silver 5 ###

# 1차: 210119
# 2차: 211002

'''
쉽게 푸는 문제
- 수학
- 구현
'''


A, B = map(int, input().split())
k = []
for i in range(1, 46):
    for j in range(i):
        k.append(i)
print(sum(k[A-1:B]))
