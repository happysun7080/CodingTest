### level 2 ###

# 1차: 221129

'''
완전탐색 - 피로도 (87946)
'''


from itertools import permutations


def solution(k, dungeons):
    results = []

    for routes in list(permutations(dungeons, len(dungeons))):
        fatigue = k
        result = 0

        for minimum, consumption in routes:
            if minimum > fatigue:
                break

            fatigue -= consumption
            result += 1

        results.append(result)

    return max(results)


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
