### Silver 4 ###

# 1차: 210126
# 2차: 220402

'''
제로
- 구현
'''


K = int(input())
r = []
for i in range(K):
    t = int(input())
    if t == 0:
        r.pop()
    else:
        r.append(t)
print(sum(r))
