### level 2 ###

# 1차: 221229

'''
그리디 - 구명보트
'''


from collections import deque

def solution(people, limit):
    answer = 0
    queue = deque(sorted(people))

    while queue:
        end = queue.pop()

        if not queue:
            answer += 1
            break

        if queue[0] + end <= limit:
            queue.popleft()
        
        answer += 1
    
    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
print(solution([30, 40, 60, 70], 100))