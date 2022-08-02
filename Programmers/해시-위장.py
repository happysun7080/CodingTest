### level 2 ###

# 1차: 220802

'''
해시 - 위장
'''

from collections import defaultdict


def solution(clothes):

    clothes_dict = defaultdict(list)
    for cloth in clothes:
        clothes_dict[cloth[1]].append(cloth[0])

    count = 1
    for key, value in clothes_dict.items():
        count *= (len(value) + 1)

    return count - 1


print(solution([["yellow_hat", "headgear"], [
      "blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], [
      "blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
