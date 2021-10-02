### level 2 ###

# 1차: 211003

'''
스택/큐 - 다리를 지나는 트럭
'''


from collections import deque


def solution(bridge_length, weight, truck_weights):

    answer = 0
    truck_passing = deque([0] * bridge_length)
    cur = 0

    while truck_passing:
        answer += 1
        cur -= truck_passing.popleft()

        if truck_weights:
            if cur + truck_weights[0] <= weight:
                cur += truck_weights[0]
                truck_passing.append(truck_weights.pop(0))
            else:
                truck_passing.append(0)


    return answer


print(solution(2,10,[7, 4, 5, 6]))
