### Silver 4 ###

# 1차: 210127
# 2차: 210922

'''
한수
- BruteForce
'''

r = 0
for i in range(1, int(input())+1):
    if len(str(i)) > 2:
        for j in range(len(str(i))-2):
            if int(str(i)[j+1])*2 != int(str(i)[j]) + int(str(i)[j+2]):
                r -= 1
                break
    r += 1
print(r)
