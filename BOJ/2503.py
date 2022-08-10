### Silver 3 ###

# 1차: 220729
# 2차: 220810

'''
숫자 야구
- 구현
'''


from itertools import permutations

num_arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
num = list(permutations(num_arr, 3))

N = int(input())
remove_count = 0

for _ in range(N):
    question, s, b = map(int, input().split())
    question = list(str(question))
    remove_count = 0

    for i in range(len(num)):
        strike = ball = 0
        i -= remove_count

        for j in range(3):
            if num[i][j] == question[j]:
                strike += 1
            elif question[j] in num[i]:
                ball += 1

        if (strike != s) or (ball != b):
            num.remove(num[i])
            remove_count += 1

print(len(num))
