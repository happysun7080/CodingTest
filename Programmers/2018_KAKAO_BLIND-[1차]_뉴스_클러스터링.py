### level 2 ###

# 1차: 220326

'''
2018 KAKAO BLIND RECRUITMENT - [1차] 뉴스 클러스터링 (17677)
'''


from collections import Counter


def multiple_set(s):
    ret = []
    for i in range(len(s) - 1):
        temp = str(s[i:i+2])
        if temp.isalpha():
            ret.append(temp.upper())
    return Counter(ret)


def solution(str1, str2):
    str1_set = multiple_set(str1)
    str2_set = multiple_set(str2)

    inter = list((str1_set & str2_set).elements())
    union = list((str1_set | str2_set).elements())

    if len(inter) == 0 and len(union) == 0:
        return 65536

    return int((len(inter) / len(union)) * 65536)


print(solution("aa1+aa2", "AAAA12"))
