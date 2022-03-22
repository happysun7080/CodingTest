### Silver 3 ###

# 1차: 220322

'''
ATM
- 그리디 알고리즘
- 정렬
'''


N = int(input())
arr = list(map(int, input().split()))
result = []

arr.sort()

for i in range(N):
    result.append(sum(arr[:i+1]))

print(sum(result))
