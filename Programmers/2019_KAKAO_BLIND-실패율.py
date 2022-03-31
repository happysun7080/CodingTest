### level 1 ###

# 1차: 220331

'''
2019 KAKAO BLIND RECRUITMENT - 오픈채팅방
'''


def solution(N, stages):

    failure = {}
    remain = len(stages)

    for stage in range(1, N+1):
        if remain == 0:
            failure[stage] = 0
        else:
            count = stages.count(stage)
            failure[stage] = count / remain
            remain -= count

    answer = sorted(failure, key=lambda x: -failure[x])

    return answer


# print(solution(4, [4, 4, 4, 4, 4]))
