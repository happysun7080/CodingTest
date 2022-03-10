### Greedy ###

'''
Q05 볼링공 고르기

level: 1/3
reference: 2019 SW 마에스트로 입학 테스트
'''

N, M = map(int, input().split())
K = list(map(int, input().split()))

rlt = 0

for i in range(N):
    B1 = K[i]
    for j in range(N-i-1):
        if B1 != K[j+i+1]:
            rlt += 1

print(rlt)
