### level 2 ###

# 1차: 221204

'''
연습문제 - 롤케이크 자르기 (132265)
'''


from collections import Counter


def solution(topping):
    answer = 0
    left, right = set(), set(topping[:])
    counter = Counter(topping)

    for t in topping:
        left.add(t)
        counter[t] -= 1

        if counter[t] == 0:
            right.remove(t)

        if len(left) == len(right):
            answer += 1

    return answer


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
print(solution([1, 2, 3, 1, 4]))
