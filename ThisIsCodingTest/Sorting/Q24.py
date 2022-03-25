### Sorting ###

'''
Q24 안테나

level: 1/3
reference: 2019 SW 마에스트로 입학 테스트 (Baekjoon 18310)
'''


N = int(input())
array = list(map(int, input().split()))
array.sort()

print(array[(N-1) // 2])
