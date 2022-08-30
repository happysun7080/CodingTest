### level 2 ###

# 1차: 220830

'''
2018 KAKAO BLIND RECRUITMENT - [1차] 프렌즈4블록 (17679)
'''


def rotate270(board):
    m = len(board)
    n = len(board[0])

    result = [[0] * m for _ in range(n)]

    for i in range(m):
        for j in range(n):
            result[n-j-1][i] = board[i][j]

    return result


def solution(m, n, board):
    answer = 0

    for i in range(m):
        board[i] = list(board[i])
    board = rotate270(board)

    while True:
        toRemove = set()
        for i in range(n-1):
            for j in range(m-1):
                cur = board[i][j]
                if cur != 'X' and cur == board[i+1][j] and cur == board[i][j+1] and cur == board[i+1][j+1]:
                    toRemove.add((i, j))
                    toRemove.add((i+1, j))
                    toRemove.add((i, j+1))
                    toRemove.add((i+1, j+1))

        removeList = list(toRemove)
        removeList.sort()
        for target in removeList:
            board[target[0]].pop(target[1])
            board[target[0]].insert(0, 'X')

        if toRemove:
            answer += (len(toRemove))
            toRemove.clear()
        else:
            break

    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC",
      "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
