### Greedy ###

'''
3-1 거스름돈

level: 1/3
'''

N = int(input())
ct = 0
coin = [500, 100, 50, 10]

for c in coin:
    ct += (N // c)
    N %= c

print(ct)
