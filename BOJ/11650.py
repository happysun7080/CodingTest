### Silver 5 ###

# 1차: 210131
# 2차: 220419

'''
좌표 정렬하기
- 정렬
'''


xy = []
for _ in range(int(input())):
    xy.append(list(map(int, input().split())))
for i in sorted(xy):
    print(i[0], i[1])
