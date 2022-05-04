### Gold 5 ###

# 1차: 210219
# 2차: 220504

'''
CCW
- 기하학
'''


x = [0, 0, 0]
y = [0, 0, 0]
for i in range(3):
    x[i], y[i] = map(int, input().split())

a = (x[0]*y[1] + x[1]*y[2] + x[2]*y[0]) - (y[0]*x[1] + y[1]*x[2] + y[2]*x[0])

if a:
    r = a//abs(a)
else:
    r = 0
print(r)
