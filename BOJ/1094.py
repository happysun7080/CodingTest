### Silver 5 ###

# 1차: 210125
# 2차: 210925

'''
막대기
- 수학
'''

X = int(input())
r = 0
for i in range(6,-1,-1):
    k = X%2**i
    if k == X: continue
    else:
        r += 1
        if k == 0: break
        else: X = k
print(r)
