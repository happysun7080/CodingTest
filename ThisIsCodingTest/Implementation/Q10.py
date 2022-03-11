### Greedy ###

'''
Q10 자물쇠와 열쇠

level: 1.5/3
reference: 2020 카카오 신입 공채 (Programmers 60057)
'''

def solution(key, lock):
    
    rlt = False

    for _ in range(4):
        key = rotate(key)
        rlt = match(key, lock)
        if rlt: break
    
    if rlt: return True
    else: return False

def rotate(k):
    N = len(k)
    rtn = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            rtn[j][N-1-i] = k[i][j]
    return rtn

def match(k, l):
    N = len(k)
    M = len(l)

    for i in range(M+N-1):
        for j in range(M+N-1):
            
            L = [[0] * (M+(N-1)*2) for _ in range(M+(N-1)*2)]

            for ii in range(N):
                for jj in range(N):
                    L[i+ii][j+jj] += k[ii][jj]
            
            flag = True
            for ii in range(M):
                for jj in range(M):
                    L[ii+(N-1)][jj+(N-1)] += l[ii][jj]
                    if L[ii+(N-1)][jj+(N-1)] != 1:
                        flag = False

            if flag: return True

    return False
            

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

