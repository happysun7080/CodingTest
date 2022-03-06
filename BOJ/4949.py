### Silver 4 ###

# 1차: 210128
# 2차: 220306

'''
균형잡힌 세상
- 자료구조
'''

while True:
    S = input()
    if S == '.': break

    r = True
    rt = []
    for i in S:
        if i == '[':
            rt += i
        elif i == '(':
            rt += i
        elif i == ']':
            if '[' not in rt:
                r = False
                break
            elif rt[-1] == '[': rt.pop()
            else:
                r = False
                break

        elif i == ')':
            if '(' not in rt:
                r = False
                break
            elif rt[-1] == '(': rt.pop()
            else:
                r = False
                break
        else:
            pass

    if r and not rt: print("yes")
    else: print("no")
