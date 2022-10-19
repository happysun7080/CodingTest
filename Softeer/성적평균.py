'''
level: 3/5 - 성적평균
'''


import sys

input = sys.stdin.readline

N, K = map(int, input().split())
score = list(map(int, input().split()))
div = []
for _ in range(K):
    div.append(list(map(int, input().split())))

for d in div:
    target = score[d[0]-1:d[1]]
    result = "{:.2f}".format(sum(target) / len(target))
    print(result)
