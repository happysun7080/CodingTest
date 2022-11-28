### level 2 ###

# 1차: 221128

'''
연습문제 - 할인 행사 (131127)
'''

from collections import defaultdict, Counter


def solution(want, number, discount):
    answer = 0
    goods = defaultdict()
    for w, n in zip(want, number):
        goods[w] = n

    for i in range(len(discount) - 10 + 1):
        if Counter(discount[i:i+10]) == goods:
            answer += 1

    return answer


print(solution(["banana", "apple", "rice", "pork", "pot"],
               [3, 2, 2, 2, 1],
               ["chicken", "apple", "apple",
                "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))

print(solution(["apple"],
               [10],
               ["banana", "banana", "banana", "banana",
                "banana", "banana", "banana", "banana", "banana", "banana"]))
