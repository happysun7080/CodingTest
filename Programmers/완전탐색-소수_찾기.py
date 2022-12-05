### level 2 ###

# 1차: 221205

'''
완전탐색 - 소수 찾기 (42839)
'''


from itertools import permutations


def solution(numbers):
    integers = [int(i) for i in numbers]
    integers_set = set()

    for i in range(1, len(numbers) + 1):
        for integer in list(permutations(integers, i)):
            number = int("".join(map(str, integer)))
            if isPrime(number):
                integers_set.add(number)

    answer = 0

    for integer in integers_set:
        if isPrime(integer):
            answer += 1

    return answer


def isPrime(integer):
    if integer < 2:
        return False

    for i in range(2, integer):
        if integer % i == 0:
            return False

    return True


print(solution("17"))
print(solution("011"))
