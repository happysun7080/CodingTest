### Silver 5 ###

# 1차: 210131
# 2차: 220422

'''
좌표 정렬하기 2
- 정렬
'''


yx = []
for _ in range(int(input())):
    yx.append(list(reversed(list(map(int, input().split())))))
for i in sorted(yx):
    print(i[1], i[0])
