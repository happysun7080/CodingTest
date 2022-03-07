### Implementation ###

'''
4-1 상하좌우
 
level: 1/3
'''

N = int(input())
Road = list(input().split())

x = y = 1

for r in Road:
    if r == 'L':
        if y != 1:
            y -= 1
    elif r == 'R':
        if y != N:
            y += 1
    elif r == 'U':
        if x != 1:
            x -= 1
    elif r == 'D':
        if x != N:
            x += 1

print(x, y)
