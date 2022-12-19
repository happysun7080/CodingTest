### Gold 5 ###

# 1차: 221219

'''
LCS
- DP
'''


stringA = input()
stringB = input()

lengthA = len(stringA)
lengthB = len(stringB)
LCS = [[0] * (lengthB + 1) for _ in range(lengthA + 1)]

for i in range(1, lengthA + 1):
    for j in range(1, lengthB + 1):
        if i == 0 or j == 0:
            continue
        elif stringA[i - 1] == stringB[j - 1]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

print(LCS[-1][-1])