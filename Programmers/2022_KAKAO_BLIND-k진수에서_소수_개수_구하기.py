# level 2 ###

# 1차: 220829

'''
2022 KAKAO BLIND RECRUITMENT - k진수에서 소수 개수 구하기 (92335)
'''

from math import sqrt


def isPrime(n):

    if n == '1':
        return False

    _n = int(n)
    for i in range(2, int(sqrt(_n))+1):
        if _n % i == 0:
            return False
    return True


def containsZero(n):
    for _n in n:
        if _n == '0':
            return True
    return False


def convertBase(n, b):
    result = ''

    while n > 0:
        n, mod = divmod(n, b)
        result += str(mod)

    return result[::-1]


def solution(n, k):
    answer = []

    rev_base = convertBase(n, k)

    for a in list(rev_base.split('0')):
        if a == '':
            continue
        if not containsZero(a) and isPrime(a):
            answer.append(a)

    return len(answer)


print(solution(437674, 3))
print(solution(110011, 10))
