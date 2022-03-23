### Sorting ###

'''
Q23 국영수

level: 1/3
reference: Baekjoon 10825
'''


N = int(input())
student = []
for _ in range(N):
    student.append(list(input().split()))

for i in range(len(student)):
    for j in range(1, 4):
        student[i][j] = int(student[i][j])

student = sorted(student, key=lambda s: (-s[1], s[2], -s[3], s[0]))

for s in student:
    print(s[0])
