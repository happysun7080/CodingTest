### level 2 ###

# 1차: 211005

'''
2019 카카오 개발자 겨울 인턴십 - 튜플
'''


def solution(s):
    answer = []
    ls = list(s[1:-1])
    ts = []
    tx = ""
    

    for l in ls:
        if l == '{':
            tx = ""
        elif l == '}':
            ts.append(tx.split(','))
        else:
            tx += l
    
    ts.sort(key=len)

    for t in ts:
        for tt in t:
            if int(tt) not in answer:
                answer.append(int(tt))
                break

    return answer


print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
