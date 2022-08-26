# level 2 ###

# 1차: 220826

'''
2021 KAKAO BLIND RECRUITMENT - 순위 검색 (72412)
'''


from collections import defaultdict
from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    answer = []
    applicant = defaultdict(list)
    for _info in info:
        i = list(map(str, _info.split(' ')))
        condition = i[:-1]
        score = int(i[-1])

        for i in range(5):
            for combination in combinations(condition, i):
                key = ''.join(combination)
                applicant[key].append(score)

    for scores in applicant.values():
        scores.sort()

    for _query in query:
        q = list(map(str, _query.replace(
            ' and ', ' ').replace('-', '').split(' ')))
        condition = ''.join(q[:-1])
        score = int(q[-1])

        count = 0
        if condition in applicant:
            scores = applicant[condition]
            index = bisect_left(scores, score)
            count = len(scores) - index

        answer.append(count)

    return answer


# def solution(info, query):
#     answer = []
#     applicant = defaultdict(lambda: defaultdict(
#         lambda: defaultdict(lambda: defaultdict(list))))
#     for _info in info:
#         i = list(map(str, _info.split(" ")))
#         applicant[i[0]][i[1]][i[2]][i[3]].append(int(i[4]))

#     for _query in query:
#         q = list(map(str, _query.replace(" and ", " ").split(" ")))

#         lang = [q[0]] if q[0] != '-' else ['cpp', 'java', 'python']
#         pos = [q[1]] if q[1] != '-' else ['backend', 'frontend']
#         career = [q[2]] if q[2] != '-' else ['junior', 'senior']
#         food = [q[3]] if q[3] != '-' else ['chicken', 'pizza']

#         score_list = []
#         for l in lang:
#             for p in pos:
#                 for c in career:
#                     for f in food:
#                         for s in applicant[l][p][c][f]:
#                             score_list.append(s)

#         count = 0
#         for s in score_list:
#             if s >= int(q[4]):
#                 count += 1

#         answer.append(count)

#     return answer

print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
      "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))
