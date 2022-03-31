### Sorting ###

'''
Q25 실패율

level: 1/3
reference: 2019 카카오 신입 공채 1차 (Programmers 42889)
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
