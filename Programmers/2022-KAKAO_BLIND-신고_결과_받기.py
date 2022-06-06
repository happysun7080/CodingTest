### level 1 ###

# 1차: 220606

'''
2022 KAKAO BLIND RECRUITMENT - 신고 결과 받기
'''

from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    id_dict = defaultdict(set)
    id_count = defaultdict(int)
    report = list(set(report))

    for r in report:
        id, rid = r.split()
        id_dict[id].add(rid)
        id_count[rid] += 1

    for id in id_list:
        cnt = 0
        for uid in id_dict[id]:
            if id_count[uid] >= k:
                cnt += 1
        answer.append(cnt)

    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], [
      "muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
