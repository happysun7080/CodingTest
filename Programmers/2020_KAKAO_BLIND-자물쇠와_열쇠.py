### level 3 ###

# 1차: 210912

'''
2020 KAKAO BLIND RECRUITMENT - 자물쇠와 열쇠
'''


def solution(key, lock):

    rlt = False

    for _ in range(4):
        key = rotate(key)
        rlt = match(key, lock)
        if rlt:
            break

    if rlt:
        return True
    else:
        return False


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

            if flag:
                return True

    return False
