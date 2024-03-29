'''
8-7 바닥 공사

level: 1.5/3
'''

# 정수 n을 입력받기
n = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0 for _ in range(1001)]

# DP 진행 (Bottom-Up)
d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] + 2*d[i-2]) % 796796

print(d(n))
