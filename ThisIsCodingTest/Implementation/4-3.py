### Implementation ###

'''
4-3 왕실의 나이트

level: 1/3
'''

K = input()

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1),
         (2, 1), (1, 2), (-1, 2), (-2, 1)]

x = int(ord(K[0])) - 96
y = int(K[1])

rlt = 0

for s in steps:
    _x = x + s[0]
    _y = y + s[1]

    if (1 <= _x <= 8) and (1 <= _y <= 8):
        rlt += 1

print(rlt)
