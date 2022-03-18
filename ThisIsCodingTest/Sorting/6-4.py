### Sorting ###

'''
6-4 퀵 정렬 1

level: 1/3
'''

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start   # pivot: 첫 번째 원소
    left = start + 1
    right = end

    while left <= right:
        # pivot보다 큰 데이터를 찾을 때 까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # pivot보다 작은 데이터를 찾을 때 까지 반복
        while right > start and array[right] > array[pivot]:
            right -= 1

        # 엇갈렸다면 작은 데이터와 pivot을 swap
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 swap
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)
