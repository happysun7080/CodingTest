### Greedy ###

'''
3-3 숫자 카드 게임

level: 1/3
reference: 2019 국가 교육기관 코딩 테스트
'''

N, M = map(int, input().split())

rlt = 0

for i in range(N):
    card = list(map(int, input().split()))

    m = min(card)
    rlt = max(rlt, m)

print(rlt)
