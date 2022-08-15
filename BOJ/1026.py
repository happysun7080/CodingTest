### Silver 4 ###

# 1차: 220815

'''
보물
- 그리디 알고리즘
- 정렬
'''


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort()

answer = 0
for a, b in zip(A, B):
    answer += (a * b)

print(answer)
