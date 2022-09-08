'''
7-6 부품 찾기 (계수 정렬)

level: 1.5/3
'''


n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    print('yes' if array[i] == 1 else 'no', end=' ')
