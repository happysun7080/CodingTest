### level 1 ###

# 1차: 210918

'''
위클리 챌린지 - 6주차 복서 정렬하기
'''


def solution(weights, head2head):
    
    stat = []

    for i, j in enumerate(weights):
        a = b = 0

        for l, k in enumerate(head2head[i]):
            if k == 'W':
                a += 1
                b += 1 if j < weights[l] else 0

        n = (len(head2head)-head2head[i].count('N'))
        e = a/n if n != 0 else 0
        stat.append((i+1, e, b, j))
    
    stat = sorted(stat, key = lambda x : (-x[1], -x[2], -x[3]))

    return [i[0] for i in stat]


print(solution([60, 70, 60], ["NNN", "NNN", "NNN"]))
