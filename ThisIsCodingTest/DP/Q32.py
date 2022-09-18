'''
Q32 정수 삼각형

level: 1.5/3
reference: IOI 1994년도 (Baekjoon 1932)
'''

T = []
N = int(input())
for i in range(N):
    T.append(list(map(int, input().split())))

for i in range(N-2, -1, -1):
    for j in range(i+1):
        T[i][j] += max(T[i+1][j], T[i+1][j+1])
print(T[0][0])
