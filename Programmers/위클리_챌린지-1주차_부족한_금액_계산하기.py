### level 1 ###

# 1차: 210908

'''
위클리 챌린지 - 1주차_부족한 금액 계산하기
'''

def solution(price, money, count):
    answer = ((count*(count+1))//2)*price - money
    return answer if answer > 0 else 0

print(solution(3, 20, 4))
