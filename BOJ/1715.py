### Gold 4 ###

# 1차: 220912

'''
카드 정렬하기
- 정렬
- 그리디 알고리즘
- 우선순위 큐
'''


import heapq

N = int(input())
heap = []
for _ in range(N):
    heapq.heappush(heap, int(input()))

rlt = []

while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    rlt.append(a+b)
    heapq.heappush(heap, (a+b))

print(sum(rlt))
