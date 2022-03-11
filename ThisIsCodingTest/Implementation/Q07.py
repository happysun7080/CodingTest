### Greedy ###

'''
Q07 럭키 스트레이트

level: 1/3
reference: Baekjoon 18406
'''

N = input()

A = B = 0

for i in range(len(N)):
    if i < len(N)//2:
        A += int(N[i])
    else:
        B += int(N[i])

if A == B:
    rlt = "LUCKY"
else:
    rlt = "READY"

print(rlt)
