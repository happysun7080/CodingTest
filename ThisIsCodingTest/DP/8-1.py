'''
8-1 피보나치 함수 (재귀)

level: 1/3
'''


def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)


print(fibo(4))
