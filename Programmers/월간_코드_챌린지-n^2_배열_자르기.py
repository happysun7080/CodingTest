### level 2 ###

# 1차: 221224

'''
월간 코드 챌린지 시즌3 - n^2 배열 자르기 (87390)
'''


def solution(n, left, right):
    targets = list(range(left, right + 1))
    answer = []
    
    for target in targets:
        answer.append(max(target // n, target % n) + 1)

    return answer

print(solution(3, 2, 5))
print(solution(4, 7, 14))