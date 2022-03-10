### Greedy ###

'''
Q01 모험가 길드

level: 1/3
reference: 핵심 유형
'''

N = int(input())
F = list(map(int, input().split()))

F.sort(reverse=True)

rlt = 0
idx = 0

while True:
    if idx < N:
        idx += F[idx]
        rlt += 1
    else:
        break

print(rlt)
