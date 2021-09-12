### level 2 ###

# 1차: 210913

'''
위클리 챌린지 - 5주차 모음 사전
'''


def solution(word):
    ans = len(word)

    idx = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    n = [781, # (((5+1)*5+1)*5+1)*5+1
         156, # ((5+1)*5+1)*5+1
         31,  # (5+1)*5+1 
         6,   # 5+1
         1]

    for i, w in enumerate(word):
        ans += n[i] * idx[w]

    return ans

print(solution(input()))
