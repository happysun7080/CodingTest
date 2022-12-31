### level 2 ###

# 1차: 230101

'''
연습문제 - 마법의 엘리베이터 (148653)
'''


def solution(storey):
    answer = 0

    while storey > 0:
        number = storey % 10
        storey //= 10
        
        if (number > 5) or (number == 5 and storey % 10 >= 5):
            answer += 10 - number
            storey += 1
        else:
            answer += number

    return answer

# print(solution(16))
# print(solution(2554))
# print(solution(5))