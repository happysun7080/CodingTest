### Silver 4 ###

# 1차: 220316

'''
에라토스테네스의 체
- 수학
- 구현
'''


import sys

input = sys.stdin.readline


def isPrime(x):
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1

    return True


N, K = map(int, input().split())

N_list = []
for i in range(2, N+1):
    N_list.append(i)

cnt = 0
i = 0
while cnt <= K:
    if N_list[i]:
        if isPrime(N_list[i]):
            value = N_list[i]
            j = i
            while j < N - 1:
                tmp = N_list[j]
                if tmp:
                    N_list[j] = 0
                    cnt += 1
                if cnt == K:
                    print(tmp)
                    exit()
                j += value
    i += 1

    
