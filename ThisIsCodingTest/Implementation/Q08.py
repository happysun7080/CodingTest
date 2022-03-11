### Greedy ###

'''
Q08 문자열 재정렬

level: 1/3
reference: Facebook 인터뷰
'''

S = input()

A = []
N = 0

for i in S:
    if 65 <= int(ord(i)) <= 90:
        A.append(i)
    else:
        N += int(i)

A.sort()
A.append(str(N))

for i in A:
    print(i, end='')
