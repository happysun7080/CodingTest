'''
Q27 정렬된 배열에서 특정 수의 개수 구하기 (이진 탐색)

level: 2/3
reference: Joho 인터뷰
'''

N, x = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = array[-1]

index = -1
while start <= end:
    mid = (start+end) // 2
    if array[mid] < x:
        start = mid + 1
    elif array[mid] > x:
        start = mid - 1
    else:
        index = mid
        break

if index == -1:
    print(-1)
    exit()

left, right = -1, 1
count = 1
while True:
    if array[index+left] == x:
        count += 1
        left -= 1
    if array[index+right] == x:
        count += 1
        right += 1
    if (array[index+left] != x and array[index+right] != x) or (index+left < 0 and index+right >= len(array)):
        break

print(count)
