'''
Q27 정렬된 배열에서 특정 수의 개수 구하기 (이진 탐색 - bisect)

level: 2/3
reference: Joho 인터뷰
'''

from bisect import bisect_left, bisect_right


def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index


N, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_range(array, x, x)
print(count if count != 0 else -1)
