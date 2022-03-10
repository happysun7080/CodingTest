### Greedy ###

'''
Q06 무지의 먹방 라이브

level: 1/3
reference: 2019 카카오 신입 공채 (Programmers 42891)
'''

import heapq


def solution(food_times, k):

    if sum(food_times) <= k:
        return -1

    food_heap = []

    for i in range(len(food_times)):
        heapq.heappush(food_heap, (food_times[i], i+1))

    sum_time = 0
    pre = 0
    len_food = len(food_times)

    while sum_time + ((food_heap[0][0] - pre) * len_food) <= k:
        now = heapq.heappop(food_heap)[0]
        sum_time += (now - pre) * len_food
        len_food -= 1
        pre = now

    rlt = sorted(food_heap, key=lambda x: x[1])
    return rlt[(k-sum_time) % len_food][1]
