'''
7-8 떡볶이 떡 만들기

level: 2/3
'''


N, M = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start+end) // 2
    for x in array:
        if x > mid:
            total += x - mid

    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
