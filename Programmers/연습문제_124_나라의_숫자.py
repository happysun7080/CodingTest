### level 2 ###

# 1차: 220804

'''
연습문제 - 124 나라의 숫자(12899)
'''


def solution(n):
    answer = ''

    while n > 0:
        n, mod = divmod(n-1, 3)
        answer += str(2**mod)

    return answer[::-1]


print(solution(1))  # 1
print(solution(2))  # 2
print(solution(3))  # 4
print(solution(4))  # 11
print(solution(5))  # 12
print(solution(6))  # 14
