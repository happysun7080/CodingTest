### Silver 4 ###

# 1차: 221125

'''
학생 번호
- 구현
'''


import sys

input = sys.stdin.readline
N = int(input())
students = []
for _ in range(N):
    students.append(input().strip())

for size in range(1, len(students[0]) + 1):
    parsed_students = set()

    for student in students:
        parsed_students.add(student[len(students[0])-size:])

    if len(parsed_students) == len(students):
        print(size)
        break
