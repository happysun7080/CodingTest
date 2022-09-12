'''
Q26 카드 정렬하기

level: 2/3
reference: Baekjoon 1715
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
