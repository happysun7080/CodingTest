### Greedy ###

'''
3-2 큰 수의 법칙

level: 1/3
reference: 2019 국가 교육기관 코딩 테스트
'''

N, M, K = map(int, input().split())
lN = list(map(int, input().split()))

lN.sort()

first = lN[-1]
second = lN[-2]

rlt = 0

while True:
    for i in range(K):
       if M == 0:
           break
       rlt += first
       M -= 1

    if M == 0:
        break

    rlt += second
    M -= 1

print(rlt)

# count = int(M/(K+1))*K + (M % (K+1))
# print(count * first + ((M-count) * second))
