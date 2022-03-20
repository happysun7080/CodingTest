### Sorting ###

'''
6-7 sorted
6-8 sort
6-9 sort - key

level: 1/3
'''

# 6-7
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)


# 6-8
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

array.sort()
print(array)


# 6-9
array = [('바나나', 2), ('사과', 5), ('당근', 3)]


def setting(data):
    return data[1]


result = sorted(array, key=setting)
print(result)
