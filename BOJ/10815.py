### Silver 4 ###

# 1차: 210213
# 2차: 220405

'''
숫자 카드
- 정렬
'''


from collections import Counter

_N = int(input())
N = Counter(map(int, input().split()))
_M = int(input())
M = list(map(int, input().split()))
for m in M:
    print(N[m], end=' ')
