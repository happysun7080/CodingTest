'''
7-1 순차 탐색 예제

level: 1/3
'''


def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1
    return -1


input_data = input().split()
array = input().split()

n = int(input_data[0])
target = input_data[1]

print(sequential_search(n, target, array))
