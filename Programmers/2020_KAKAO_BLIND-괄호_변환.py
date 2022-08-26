# level 2 ###

# 1차: 220826

'''
2020 KAKAO BLIND RECRUITMENT - 괄호 변환 (60058)
'''


def isCorrect(s):
    count = 0
    for _s in s:
        if _s == '(':
            count += 1
        else:
            if count < 1:
                return False
            count -= 1

    return True


def getUV(p):
    a, b = 0, 0
    for i, _p in enumerate(list(p)):
        if _p == '(':
            a += 1
        else:
            b += 1
        if a == b:
            return str(p[:i+1]), str(p[i+1:])


def solution(p):

    if not p or isCorrect(p):
        return p

    u, v = getUV(p)

    if isCorrect(u):
        return u + solution(v)
    else:
        answer = '(' + solution(v) + ')'

        for s in u[1:len(u)-1]:
            answer += '(' if s == ')' else ')'

    return answer


print(solution("(()())()"))  # "(()())()"
print("-----")
print(solution(")("))  # "()"
print("-----")
print(solution("()))((()"))  # "()(())()"
print("-----")
print(solution(")))((("))  # "()(())()"
