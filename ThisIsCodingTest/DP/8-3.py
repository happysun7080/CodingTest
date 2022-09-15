'''
8-3 피보나치 수열 (재귀 - 호출되는 함수 확인)

level: 1/3
'''

d = [0 for _ in range(100)]


def pibo(x):
    print('f(' + str(x) + ')', end=' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = pibo(x-1) + pibo(x-2)
    return d[x]


pibo(6)
