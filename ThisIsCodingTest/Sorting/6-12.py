### Sorting ###

'''
6-12 두 배열의 원소 교체

level: 1/3
reference: 국제 알고리즘 대회
'''


n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
