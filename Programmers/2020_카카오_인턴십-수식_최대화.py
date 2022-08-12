### level 2 ###

# 1차: 220811

'''
2020 카카오 인턴십 - 수식 최대화 (67257)
'''

from copy import deepcopy
from itertools import permutations


def do_op(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b


def solution(expression):
    answer = []
    op_cand = ['+', '-', '*']
    op_list = []
    num_cand = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    exp_list = []

    num = ""
    for i, s in enumerate(expression):
        if s in op_cand:
            if expression[i-1] != '-':
                if s not in op_list:
                    op_list.append(s)
                exp_list.append(int(num))
                exp_list.append(s)
                num = ""
            else:
                num += s
        if s in num_cand:
            num += s

    exp_list.append(int(num))
    op_list = list(permutations(op_list, len(op_list)))

    for op in op_list:
        new_exp_list = deepcopy(exp_list)
        for o in op:
            new_list = []
            do_op_flag = False
            for i, s in enumerate(new_exp_list):
                if s == o:
                    a = new_list.pop()
                    b = new_exp_list[i+1]
                    new_list.append(do_op(a, s, b))
                    do_op_flag = True
                else:
                    if do_op_flag:
                        do_op_flag = False
                    else:
                        new_list.append(s)
            new_exp_list = new_list
        answer.append(abs(new_exp_list[0]))

    return max(answer)


# print(solution("100-200*300-500+20"))  # 60420
# print(solution("50*6-3*2"))  # 300
