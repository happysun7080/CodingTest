### Sorting ###

'''
6-5 퀵 정렬 2

level: 1/3
'''

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    if len(array) < 1:
        return array

    pivot = array[0]    # pivot: 첫 번째 원소
    tail = array[1:]    # tail: pivot을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]  # 분할 된 오른쪽 부분

    # 분할 이후 left_side와 right_side에서 각자 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))
