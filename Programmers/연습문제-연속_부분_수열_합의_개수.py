### level 2 ###

# 1차: 221129

'''
연습문제 - 연속 부분 수열 합의 개수 (131701)
'''


def solution(elements):
    total = set()

    for size in range(1, len(elements) + 1):
        for comb in circularCombs(elements, size):
            total.add(sum(comb))

    return len(total)


def circularCombs(elements, size):
    result = []

    for i in range(len(elements)):
        if i + size > len(elements):
            tmp = elements[i:]
            tmp += (elements[:i + size - len(elements)])
            result.append(tmp)
        else:
            result.append(elements[i:i+size])

    return result


print(solution([7, 9, 1, 1, 4]))
