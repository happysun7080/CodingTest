### Silver 3 ###

# 1차: 210128
# 2차: 211115

'''
프린터 큐
- 구현
- 자료구조
'''


for _ in range(int(input())):
    N,M = map(int,input().split())
    vI = list(map(int,input().split()))
    kI = list(range(N))

    r = 0
    while True:
        if vI[0] == max(vI):
            r += 1
            if kI[0] == M:
                print(r)
                break
            else:
                vI.pop(0)
                kI.pop(0)
        else:
            vI.append(vI[0])
            vI.pop(0)
            kI.append(kI[0])
            kI.pop(0)
