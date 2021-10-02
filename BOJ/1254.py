### Silver 1 ###

# 1차: 210204
# 2차: 211002

'''
팰린드롬 만들기
- BruteForce
- 문자열
'''


S = input()
s = len(S)

for i in range(s):
    if S[i:] == S[i:][::-1]:
        print(s+i)
        break
