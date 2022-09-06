### Gold 5 ###

# 1차: 220905

'''
평범한 배낭
- DP
'''


from collections import defaultdict

N, K = map(int, input().split())
bag = defaultdict(int)
bag[0] = 0
for _ in range(N):
    W, V = map(int, input().split())
    temp = defaultdict(int)
    for w, v in bag.copy().items():
        if W+w <= K and V+v > bag[W+w]:
            temp[W+w] = V+v
    bag.update(temp)

print(max(bag.values()))
