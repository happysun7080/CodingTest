'''
Q28 고정점 찾기

level: 1.5/3
reference: Amazon 인터뷰
'''

N = int(input())
array = list(map(int, input().split()))

start = 0
end = len(array)

fixed_point = -1
while start <= end:
    mid = (start+end) // 2
    if array[mid] < mid:
        start = mid + 1
    elif array[mid] > mid:
        end = mid - 1
    else:
        fixed_point = mid
        break

print(fixed_point)
