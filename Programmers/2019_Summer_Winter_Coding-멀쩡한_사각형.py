### level 2 ###

# 1차: 220803

'''
Summer/Winter Coding(2019) - 멀쩡한 사각형
'''

import math


def solution(w, h):

    gcd_wh = math.gcd(w, h)
    print(gcd_wh)
    g_w = w // gcd_wh
    g_h = h // gcd_wh

    return w * h - ((g_w + g_h-1) * gcd_wh)


# print(solution(8, 12))  # 80
