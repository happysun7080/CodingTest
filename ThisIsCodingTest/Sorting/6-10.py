### Sorting ###

'''
6-10 위에서 아래로

level: 1/3
reference: T 기업 코딩 테스트
'''


array = []
for _ in range(int(input())):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')
