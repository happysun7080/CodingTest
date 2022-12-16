### level 2 ###

# 1차: 221217

'''
연습문제 - 디펜스 게임 (142085)
'''


import heapq


def solution(n, k, enemy):
    total, answer = 0, 0
    heap = []
    
    for e in enemy:
        total += e

        if total <= n:
            heapq.heappush(heap, -e)
            answer += 1
        elif k > 0:
            k -= 1
            total += heapq.heappushpop(heap, -e)
            answer += 1
        else:
            break

    return answer