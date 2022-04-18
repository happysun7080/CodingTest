### Silver 5 ###

# 1차: 210126
# 2차: 220418

'''
Base Conversion
- 구현
- 수학
'''


A, B = map(int, input().split())
N = int(input())
_A = list(map(int, input().split()))
_A.reverse()
_B = []

k = r = 0
for i in range(len(_A)):
    k += _A[i] * (A ** i)
for i in range(21):
    if k % B**i == k:
        r = i
        break
for i in range(r-1, -1, -1):
    _B.append(k // B ** i)
    k %= B ** i

for i in _B:
    print(i, end=' ')
