'''
8-6 개미 전사

level: 2/3
'''

# 정수 n, 식량 정보 입력받기
n = int(input())
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0 for _ in range(100)]

# DP 진행 (Bottom-Up)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])
