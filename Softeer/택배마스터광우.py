'''
level: 3/5 - 택배 마스터 광우
'''

from itertools import permutations
import sys
input = sys.stdin.readline


N, M, K = map(int, input().split())
rails = list(map(int, input().split()))
rails = permutations(rails, N)
results = []


for rail in list(rails):
    count, result, index = 0, 0, 0

    while count < K:
        basket = 0

        while basket + rail[index] <= M:
            basket += rail[index]
            index += 1

            if index >= N:
                index = 0
        
        count += 1
        result += basket
    
    results.append(result)

print(min(results))