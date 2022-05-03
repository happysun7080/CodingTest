### level 2 ###

# 1차: 220504

'''
스택/큐 - 기능개발
'''


def solution(progresses, speeds):
    answer = []
    new_prog = progresses
    cnt = 0

    while(len(new_prog) > 0):
        new_prog = [i+j for i, j in zip(new_prog, speeds)]

        while (len(new_prog) > 0) and (new_prog[0] >= 100):
            new_prog.pop(0)
            speeds.pop(0)
            cnt += 1
        if cnt != 0:
            answer.append(cnt)
        cnt = 0

    return answer


# print(solution([93, 30, 55], [1, 30, 5]))
# print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
