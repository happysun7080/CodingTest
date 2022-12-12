'''
10-2 경로 압축 기법

level: 1/3
'''


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]
