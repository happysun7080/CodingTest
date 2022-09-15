'''
8-8 효율적인 화폐 구성

level: 1.5/3
'''

# 정수 N, M, 화폐 단위 정보 입력받기
n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001 for _ in range(m+1)]

# DP 진행 (Bottom-Up)
d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]]+1)

print(d[m] if d[m] != 10001 else -1)
