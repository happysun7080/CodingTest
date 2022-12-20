### Gold 5 ###

# 1차: 221220

'''
A와 B
- 구현
- 그리디 알고리즘
'''


S = list(input())
T = list(input())

while len(T) > len(S):
    last = T.pop()

    if last == 'B':
        T.reverse()

print(1 if T == S else 0)
