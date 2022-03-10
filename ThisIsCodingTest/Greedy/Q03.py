### Greedy ###

'''
Q03 문자열 뒤집기

level: 1/3
reference: Baekjoon 1439
'''

S = input()

tmp = f = S[0]
rlt = 0

for i in S:
    if tmp != i:
        if tmp == f:
            rlt += 1
        tmp = i

print(rlt)
