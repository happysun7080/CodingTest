### Silver 4 ###

# 1차: 210213
# 2차: 220413

'''
중복 빼고 정렬하기
- 정렬
'''


N = int(input())
S = list(map(int, input().split()))
S.sort()
print(S[0], end=' ')
for i in range(1, N):
    if S[i] != S[i-1]:
        print(S[i], end=' ')
