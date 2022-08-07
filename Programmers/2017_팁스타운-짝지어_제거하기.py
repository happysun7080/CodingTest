### level 2 ###

# 1차: 220803 (SOLVING)

'''
힙(Heap) - 더 맵게(42626)
'''


def solution(s):
    s_list = []

    for s_i in s:
        if not s_list:
            s_list.append(s_i)
            continue
        if s_i == s_list[-1]:
            s_list.pop()
        else:
            s_list.append(s_i)

    return 0 if s_list else 1


print(solution('cbaabaac'))  # 1
print(solution('cdcd'))  # 0
print(solution('aaa'))  # 0
