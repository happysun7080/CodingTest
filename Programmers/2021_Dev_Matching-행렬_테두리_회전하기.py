### level 2 ###

# 1차: 211031

'''
2021 Dev-Matching: 웹 백엔드 개발자(상반기) - 행렬 테두리 회전하기
'''


def solution(rows, columns, queries):
    answer = []
    matrix = [[0] * columns for _ in range(rows)]
    
    # create initial matrix
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = i*columns + j + 1

    # main loop
    while(queries):
        query = queries.pop(0)
        x1 = query[0]-1; y1 = query[1]-1; x2 = query[2]-1; y2 = query[3]-1;
        x = query[0] - 1
        y = query[1] - 1

        elements  = []
        order     = []
        
        # store elements to be rotated
        while(True):
            elements.append(matrix[x][y])
            order.append((x, y))

            if x == x1 and y < y2:
                y += 1
            elif x < x2 and y == y2:
                x += 1
            elif x == x2 and y > y1:
                y -= 1
            elif x > x1 and y == y1:
                x -= 1
            
            if x == x1 and y == y1:
                break

        answer.append(min(elements))

        # do rotate
        for i, ord in enumerate(order):
            matrix[ord[0]][ord[1]] = elements[(i-1) % len(elements)]


    return answer


print(solution(100,97,[[1, 1, 100, 97]]))

