### level 2 ###

# 1차: 221221

'''
연습문제 - 점 찍기 (140107)
'''


def solution(k, d):
    answer = 0

    for y in range(d + 1):
        x = int((d ** 2 - y ** 2) ** 0.5)

        if y % k == 0:
            answer += x // k + 1

    return answer

print(solution(2, 4))
print(solution(1, 5))