### level 3 ###

# 1차: 220908

'''
2020 KAKAO BLIND RECRUITMENT - 외벽 점검 (60062)
'''


from itertools import permutations


def solution(n, weak, dist):
    weak_size = len(weak)
    answer = []
    weak_linear = weak + [w+n for w in weak]

    for i, start in enumerate(weak):
        for friends in permutations(dist):
            count = 1
            pos = start
            for friend in friends:
                pos += friend
                if pos < weak_linear[i+weak_size-1]:
                    count += 1
                    pos = [w for w in weak_linear[i+1:i+weak_size] if w > pos][0]
                else:
                    answer.append(count)
                    break

    return min(answer) if answer else -1


# print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))  # 2
# print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))  # 1
