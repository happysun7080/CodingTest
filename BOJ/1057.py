### Silver 3 ###

# 1차: 210122
# 2차: 210914

'''
토너먼트
- 수학
- BruteForce
'''

N, A, B = map(int, input().split())

for i in range(N//2 + N % 2):
    a = A//2 + A % 2
    b = B//2 + B % 2
    if a == b:
        print(i+1)
        exit()
    else:
        A = a
        B = b

print(-1)
