### Greedy ###

'''
Q02 곱하기 혹은 더하기

level: 1/3
reference: Facebook 인터뷰
'''

S = input()

rlt = int(S[0])

for i in range(len(S)-1):
    m = rlt * int(S[i+1])
    p = rlt + int(S[i+1])

    if m > p:
        rlt *= int(S[i+1])
    else:
        rlt += int(S[i+1])

print(rlt)
