### Greedy ###

'''
Q12 기둥과 보 설치

level: 1.5/3
reference: 2020 카카오 신입 공채 (Programmers 60061)
'''


def check(answer):
    for x, y, a in answer:
        if a == 0:
            if y != 0 and [x, y-1, 0] not in answer and [x-1, y, 1] not in answer and [x, y, 1] not in answer:
                return True
        else:
            if [x, y-1, 0] not in answer and [x+1, y-1, 0] not in answer and not ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                return True
    return False


def solution(n, build_frame):
    answer = []

    for x, y, a, b in build_frame:
        struct = [x, y, a]

        if b == 1:
            answer.append(struct)
            if check(answer):
                answer.remove(struct)
        else:
            if struct in answer:
                answer.remove(struct)
                if check(answer):
                    answer.append(struct)

    answer.sort()
    return answer


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [
      5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [
      1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
