### level 2 ###

# 1차: 220807

'''
2021 KAKAO BLIND RECRUITMENT - 메뉴 리뉴얼 (72411)
'''

from itertools import combinations


def solution(orders, course):
    answer = []

    orders_comb = dict()
    orders_count = dict()

    for order in orders:
        for i in range(len(order)+1):
            for comb in list(combinations(sorted(order), i)):
                if len(comb) < 2:
                    continue
                if comb in orders_comb:
                    orders_comb[comb] += 1
                else:
                    orders_comb[comb] = 1

    for c in course:
        orders_count[c] = []

    for key, value in orders_comb.items():
        if len(key) in course and value >= 2:
            orders_count[len(key)].append(["".join(key), value])

    for _, value in orders_count.items():
        if not value:
            continue
        value_sorted = sorted(value, key=lambda x: -x[1])
        max_counted = value_sorted[0][1]
        for v in value_sorted:
            if v[1] == max_counted:
                answer.append(v[0])

    return sorted(answer)


# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
# print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
