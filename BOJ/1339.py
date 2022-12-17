### Gold 4 ###

# 1차: 221218

'''
단어 수학
- 그리디 알고리즘
'''


from collections import defaultdict


N = int(input())
words = [input() for _ in range(N)]
dic = defaultdict(int)
answer = 0

for word in words:
    for i, w in enumerate(reversed(word)):
        dic[w] += 10 ** i

alphabets = list(dic.values())

for alphabet, number in zip(sorted(alphabets, reverse=True), range(9, 9 - len(alphabets), -1)):
    answer += alphabet * number

print(answer)
