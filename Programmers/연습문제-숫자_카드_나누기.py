### level 2 ###

# 1차: 221202

'''
연습문제 - 숫자 카드 나누기 (135807)
'''


def solution(arrayA, arrayB):
    gcdA = gcdArray(arrayA)
    resultA = gcdA

    for b in arrayB:
        if b % gcdA == 0:
            resultA = gcdA // gcd(b, gcdA)

    gcd_B = gcdArray(arrayB)
    resultB = gcd_B

    for a in arrayA:
        if a % gcd_B == 0:
            resultB = gcd_B // gcd(a, gcd_B)

    return resultA if resultA > resultB else resultB if resultA < resultB else 0


def gcd(a, b):
    r = b % a
    if r == 0:
        return a
    return gcd(r, a)


def gcdArray(array):
    result = array[0]
    for i in array:
        result = gcd(result, i)

    return result


print(solution([10, 17], [5, 20]))
print(solution([10, 20], [5, 17]))
print(solution([14, 35, 119], [18, 30, 102]))
