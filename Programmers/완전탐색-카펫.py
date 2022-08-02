### level 2 ###

# 1차: 220802

'''
완전탐색 - 카펫 (42842)
'''


def getSubMul(x):
    sub_list = []

    if x == 1:
        return [[1, 1]]

    for i in range(1, x//2 + 1):
        if x % i == 0:
            sub_list.append([i, x//i])

    return sub_list


def solution(brown, yellow):

    yellow_sub_list = getSubMul(yellow)
    for yellow_sub in yellow_sub_list:
        yellow_sub.sort(reverse=True)
        x, y = max(yellow_sub), min(yellow_sub)
        if (x+2) * (y+2) - (x*y) == brown:
            return [x+2, y+2]

    return []


# print(solution(10, 2))  # [4, 3]
# print(solution(8, 1))   # [3, 3]
# print(solution(24, 24))  # [8, 6]
