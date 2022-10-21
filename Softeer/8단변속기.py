'''
level: 2/5 - 8단 변속기
'''


import sys

input = sys.stdin.readline
gears = list(map(int, input().split()))

if gears == list(range(1, 9)):
    print("ascending")
elif gears == list(range(8, 0, -1)):
    print("descending")
else:
    print("mixed")
