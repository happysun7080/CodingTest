### Implementation ###

'''
4-2 시각

level: 1/3
'''

N = int(input())

rlt = 0

for i in range(N + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                rlt += 1

print(rlt)
