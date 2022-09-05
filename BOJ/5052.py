### Gold 4 ###

# 1차: 220905

'''
전화번호 목록
- 해시
- 문자열
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


for _ in range(int(input())):
    phone_book = []
    for _ in range(int(input())):
        phone_book.append(input())
    if solution(phone_book):
        print('YES')
    else:
        print('NO')
