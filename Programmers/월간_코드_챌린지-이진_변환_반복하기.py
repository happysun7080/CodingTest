### level 2 ###

# 1차: 221225

'''
월간 코드 챌린지 시즌1 - 이진 변환 반복하기 (70129)
'''


def solution(s):
    iter, zero = 0, 0

    while s != "1":
        iter += 1
        zero += list(s).count("0")

        counts = list(s).count("1")
        s = bin(counts)[2:]

    return [iter, zero]


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))