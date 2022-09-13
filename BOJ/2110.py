### Gold 4 ###

# 1차: 210812
# 2차: 220913

'''
공유기 설치
- 이분 탐색
'''


import sys

input = sys.stdin.readline

N, C = map(int, input().split())
h = []
for _ in range(N):
    h.append(int(input()))

h.sort()

start = 1
end = h[-1] - h[0]

while end >= start:
    mid = (end+start) // 2
    value = h[0]
    count = 1

    for i in range(1, N):
        if h[i] >= value + mid:
            value = h[i]
            count += 1

    if count >= C:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)
