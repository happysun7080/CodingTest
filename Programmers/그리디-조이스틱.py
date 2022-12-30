### level 2 ###

# 1차: 221231

'''
그리디 - 조이스틱
'''


def solution(name):
    answer, move = 0, len(name) - 1
    dic = {}

    for i in range(ord('A'), ord('Z') + 1):
        dic[chr(i)] = min(i - ord('A'), ord('A') + 26 - i)

    for n in name:
        answer += dic[n]

    for i, n in enumerate(name):
        a = i + 1

        while a < len(name) and name[a] == 'A':
            a += 1
        
        move = min([
            move, 
            2 * i + len(name) - a, 
            2 * (len(name) - a) + i
        ])

    return answer + move


print(solution("JEROEN"))
print(solution("JAN"))
print(solution("BCDAAAACB"))
