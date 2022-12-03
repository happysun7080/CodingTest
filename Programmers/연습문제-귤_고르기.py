### level 2 ###

# 1차: 221202

'''
연습문제 - 귤 고르기 (138476)
'''


from collections import Counter


def solution(k, tangerine):
    answer, count = 0, 0
    counter = list(Counter(tangerine).values())
    counter.sort(reverse=True)

    for i in counter:
        if count + i >= k:
            answer += 1
            break

        count += i
        answer += 1

    return answer


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))  # 3
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))  # 2
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))  # 1
