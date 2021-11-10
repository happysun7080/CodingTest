### Silver 2 ###

# 1차: 210127
# 2차: 211110

'''
소수 구하기
- 수학
'''

M, N = map(int, input().split())

pc = [1 for _ in range(N-1)]  # 2,3,4,...,N
for i in range(N-1):
    if pc[i]:
        if i+2 >= M:
            print(i+2)
        for j in range((i+1)*2, N-1, i+2):
            pc[j] = 0
