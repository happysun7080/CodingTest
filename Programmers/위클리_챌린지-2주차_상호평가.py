### level 1 ###

# 1차: 210908

'''
위클리 챌린지 - 2주차 상호평가
'''

def getGrade(score):
    if score >= 90: return 'A'
    elif 80 <= score < 90: return 'B'
    elif 70 <= score < 80: return 'C'
    elif 50 <= score < 70: return 'D'
    else: return 'F'



def solution(scores):
    answer = ''

    for i in range(len(scores)):
        l = len(scores)
        s = [j[i] for j in scores]
        sc = sum(s)

        if s[i] == min(s) or s[i] == max(s):
            if s.count(s[i]) == 1:
                sc -= s[i]
                l -= 1

        answer += getGrade(sc/l)

    return answer


a = [[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [
    47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]
print(solution(a))

