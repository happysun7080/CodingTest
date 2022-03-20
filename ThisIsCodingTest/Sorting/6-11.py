### Sorting ###

'''
6-11 성적이 낮은 순서로 학생 출력하기

level: 1/3
reference: D 기업 프로그래밍 콘테스트 예선
'''


array = []
for _ in range(int(input())):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')
