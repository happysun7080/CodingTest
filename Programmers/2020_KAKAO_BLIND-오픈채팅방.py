### level 2 ###

# 1차: 220307

'''
2019 KAKAO BLIND RECRUITMENT - 오픈채팅방
'''


def solution(record):
    answer = []
    rec_dic = {}

    for rec in record:
        r = rec.split()
        if r[0] in ['Enter', 'Change']:
            rec_dic[r[1]] = r[2]

    for rec in record:
        r = rec.split()
        if r[0] == 'Enter':
            answer.append(rec_dic[r[1]] + '님이 들어왔습니다.')
        elif r[0] == 'Leave':
            answer.append(rec_dic[r[1]] + '님이 나갔습니다.')

    return(answer)

# print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
