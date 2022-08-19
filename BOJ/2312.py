### Silver 3 ###

# 1차: 220819

'''
수 복원하기
- 수학
'''


def getFactorPrime(x):
    factors = []
    factor = 2

    while (factor**2 <= x):
        while (x % factor == 0):
            factors.append(factor)
            x //= factor
        factor += 1

    if x > 1:
        factors.append(x)

    return factors


def printFactorPrime(x):
    for prime in getFactorPrime(x):
        count = 0
        while(x % prime == 0):
            x //= prime
            count += 1

        if count != 0:
            print(prime, count)


N = int(input())
for _ in range(N):
    printFactorPrime(int(input()))
