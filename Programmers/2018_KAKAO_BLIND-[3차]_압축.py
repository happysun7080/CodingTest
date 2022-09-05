### level 2 ###

# 1차: 220905

'''
2018 KAKAO BLIND RECRUITMENT - [3차] 압축 (17684)
'''


from collections import defaultdict


def solution(msg):
    answer = []
    dictionary = defaultdict(int)
    for i in range(65, 65+26):
        dictionary[chr(i)] = i - 64

    i, d = 0, 27
    while i < len(msg):
        size = 1
        while dictionary[msg[i:i+size]] != 0:
            size += 1
            if i+size > len(msg):
                break
        if dictionary[msg[i:i+size]] == 0:
            dictionary[msg[i:i+size]] = d

        answer.append(dictionary[msg[i:i+size-1]])
        i += size-1
        d += 1

    return answer


print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))
print(solution('ABABABABABABABAB'))
