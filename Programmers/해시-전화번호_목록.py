### level 2 ###

# 1차: 220825

'''
해시 - 전화번호 목록
'''


def solution(phone_book):

    book = dict()
    for phone_num in phone_book:
        book[phone_num] = 0

    for phone_num in phone_book:
        tmp = ""
        for num in phone_num:
            tmp += num
            if tmp in book and tmp != phone_num:
                return False

    return True
