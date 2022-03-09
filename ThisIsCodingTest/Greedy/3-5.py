### Greedy ###

'''
3-5 1이 될 때까지

level: 1/3
reference: 2018 E 기업 알고리즘 대회
'''

N, K = map(int, input().split())

rlt = 0

while True:
    if N == 1:
        break

    if N % K != 0:
        N -= 1
    else:
        N //= K

    rlt += 1

print(rlt)
