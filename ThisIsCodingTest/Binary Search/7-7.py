'''
7-6 부품 찾기 (집합 자료형)

level: 1.5/3
'''


n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    print('yes' if i in array else 'no', end=' ')
