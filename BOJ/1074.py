### Silver 1 ###

# 1차: 210126
# 2차: 210923

'''
Z
- Divide and Conquer
- Recursion
'''

N, r, c = map(int, input().split())

ra = 0
rb = 2**N
ca = 0
cb = 2**N
rlt = 0
for _ in range(16):
    if ra == r and ca == c:
        print(rlt)
        break

    k = ((rb - ra) // 2) ** 2

    if ca <= c < (ca + cb)//2 and ra <= r < (ra + rb) // 2:  # 1사분면
        cb = (ca+cb)//2
        rb = (ra+rb)//2
        continue

    if (ca + cb)//2 <= c < cb and ra <= r < (ra + rb) // 2:  # 2사분면
        rlt += k
        ca = (ca+cb)//2
        rb = (ra+rb)//2
        continue

    if ca <= c < (ca + cb)//2 and (ra + rb) // 2 <= r < rb:  # 3사분면
        rlt += k * 2
        cb = (ca+cb)//2
        ra = (ra+rb)//2
        continue

    if (ca + cb)//2 <= c < cb and (ra + rb) // 2 <= r < rb:  # 4사분면
        rlt += k * 3
        ca = (ca+cb)//2
        ra = (ra+rb)//2
        continue

# p=[0,0]
# for i in range(4**N):
#     if p == [r,c]:
#         print(i)
#         break
#     if (i+1)%2:
#         p[1] += 1
#         continue
#
#     for j in range(N*2-1,0,-1):
#         if (i+1)%(2**j) == 0:
#             if j == 1 or j == 2:
#                 p[0] += (-1)**(j-1)
#                 p[1] += (-1)**j
#             else:
#                 if j%2 == 0:
#                     p[0] -= 2**(j//2 + j%2) - 1
#                     p[1] += 1
#                 else:
#                     p[0] += 1
#                     p[1] -= 2 ** (j // 2 + j % 2) - 1
#             break
