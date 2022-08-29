# level 2 ###

# 1차: 220826

'''
2019 KAKAO BLIND RECRUITMENT - 후보키 (42890)
'''


from itertools import combinations


def isUnique(row):
    return True if len(row) == len(set(row)) else False


def isMinimalUnique(answer, row):
    for ans in answer:
        if all(x in row for x in ans):
            return False
    return True


def isMinimalRelation(row, rows):

    _rows = []
    for i in row:
        _rows.append(rows[i])

    new_rows = []
    for i in range(len(_rows[0])):
        new_rows.append([x[i] for x in _rows])

    new_row = []
    for r in new_rows:
        new_row.append(''.join(r))

    return isUnique(new_row)


def solution(relation):
    answer = []
    size = len(relation[0])

    rows = []
    for i in range(size):
        row = [x[i] for x in relation]
        if isUnique(row):
            answer.append([i])
        rows.append(row)

    _combination, combination = [], []
    for i in range(2, size+1):
        _combination.append(list(combinations(range(size), i)))
    for comb in _combination:
        for c in comb:
            combination.append(list(c))

    for comb in combination:
        if isMinimalUnique(answer, comb) and isMinimalRelation(comb, rows):
            answer.append(comb)

    return len(answer)


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], [
      "400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
