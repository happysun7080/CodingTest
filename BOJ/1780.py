### Silver 2 ###

# 1차: 220831

'''
종이의 개수
- 분할 정복
'''


import sys

input = sys.stdin.readline
count = {}
count[-1] = 0
count[0] = 0
count[1] = 0


def isPaper(paper):
    target = paper[0][0]
    if len(paper) == 1:
        return target
    for i in paper:
        for j in i:
            if j != target:
                return 100
    return target


def solution(paper, n):
    is_paper = isPaper(paper)
    if is_paper != 100:
        count[is_paper] += 1
        return

    size = n // 3
    for i in [0, size, size*2]:
        for j in [0, size, size*2]:
            div_paper = [row[j:j+size] for row in paper[i:i+size]]
            solution(div_paper, size)


N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

solution(paper, N)

for _, value in count.items():
    print(value)
