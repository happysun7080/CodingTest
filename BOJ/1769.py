### Silver 5 ###

# 1차: 210119
# 2차: 211107

'''
3의 배수
- 구현
'''


X = input()
r = 0
while True:
    if int(X) >= 10:
        c = 0
        for i in X:
            c += int(i)
        X = str(c)
        r += 1
        continue
    else:
        print(r)
        if int(X) % 3:
            print('NO')
        else:
            print('YES')
        break
