### Silver 3 ###

# 1차: 210717
# 2차: 220325

'''
안테나
- 정렬
- 수학
'''


N = int(input())
array = list(map(int, input().split()))
array.sort()

print(array[(N-1) // 2])
