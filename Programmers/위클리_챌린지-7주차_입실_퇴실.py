### level 2 ###

# 1차: 210915

'''
위클리 챌린지 - 7주차 모음 사전
'''


from collections import deque

def solution(enter, leave):
    
    cnt = [[0] * (len(enter)+1) for _ in range(len(enter)+1)]
    ent = []
    lve = []

    enter = deque(enter)
    leave = deque(leave)

    while leave: 
        # leave 차례
        if leave[0] in ent:
            ent.remove(leave[0])
            lve.append(leave.popleft())
        # enter 차례
        else: 
            newent = enter.popleft()
            for e in ent:
                cnt[e][newent] += 1
                cnt[newent][e] += 1
            ent.append(newent)

    answer = list(map(lambda i: sum(i), cnt))
    return answer[1:]


print(solution([1, 4, 2, 3], [2, 1, 3, 4]))
