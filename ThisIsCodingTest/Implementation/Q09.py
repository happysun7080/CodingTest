### Greedy ###

'''
Q09 문자열 압축

level: 1.5/3
reference: 2020 카카오 신입 공채 (Programmers 60057)
'''

def solution(input_str):

    len_list = []
    len_list.append(len(input_str))

    for i in range(1, len(input_str)//2 + 1):
        rest = len(input_str) % i
        s = input_str[:len(input_str)-rest]

        list_s = []
        for j in range(len(s)//i):
            list_s.append(s[j*i:j*i+i])

        tok = list_s[0]
        cnt = 1
        cur_len = rest

        for j in range(1,len(list_s)):
            if tok == list_s[j]:
                cnt += 1
            else:
                if cnt > 1:
                    cur_len += len(str(cnt)+tok)
                    cnt = 1
                else:
                    cur_len += len(tok)
                tok = list_s[j]

            if j == len(list_s)-1:
                if cnt > 1:
                    cur_len += len(str(cnt)+tok)
                else:
                    cur_len += len(tok)

        len_list.append(cur_len)
        
    return min(len_list)


# print(solution(input()))
