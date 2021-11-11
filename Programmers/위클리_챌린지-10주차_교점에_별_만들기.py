from itertools import combinations

def solution(line):
    N = [i for i in range(len(line))]
    answer    = []
    i_points  = []
    list_x, list_y = [], []

    for i, j in combinations(N, 2):
        a, b, e = line[i]
        c, d, f = line[j]
    
        if a*b-b*c == 0: continue

        x = (b*f-e*d)/(a*d-b*c)
        y = (e*c-a*f)/(a*d-b*c)

        if x.is_integer() and y.is_integer():
            i_points.append((int(x), int(y)))
            list_x.append(int(x))
            list_y.append(int(y))

    max_x = max(list_x)
    min_x = min(list_x)
    max_y = max(list_y)
    min_y = min(list_y)                  

    size_x = max_x - min_x + 1
    size_y = max_y - min_y + 1
    board = [["."] * size_x for _ in range(size_y)]

    for x, y in i_points:
        board[max_y - y][x - min_x] = "*"

    for b in board: answer.append(''.join(b))

    return answer


print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))
