### level 2 ###

# 1차: 220804

'''
힙(Heap) - 더 맵게(42626)
'''

import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while len(scoville) >= 2:
        a = heapq.heappop(scoville)
        if a >= K:
            return answer

        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + (b*2))
        answer += 1

    return answer if scoville[0] > K else -1


# print(solution([1, 2, 3, 9, 10, 12], 7))  # 2
