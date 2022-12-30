### level 2 ###

# 1차: 221230

'''
그리디 - 큰 수 만들기
'''


def solution(number, k):
    answer = [number[0]]

    for num in number[1:]:
        if k > 0:
            while answer[-1] < num:
                answer.pop()
                k -= 1

                if not answer or k <= 0:
                    break

        answer.append(num)

    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))