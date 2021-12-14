### Silver 5 ###

# 1차: 210128
# 2차: 211214

'''
최대공약수와 최소공배수
- 수학
'''


from math import gcd

N = list(map(int, input().split()))
A, B = max(N), min(N)
print(gcd(A, B))
print(A*B//gcd(A, B))
