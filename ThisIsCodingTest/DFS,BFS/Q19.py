'''
Q19 연산자 끼워 넣기

level: 2/3
reference: 삼성전자 SW 역량테스트 (Baekjoon 14888)
'''


# from itertools import permutations


# N = int(input())
# nums = list(map(int, input().split()))
# op_count = list(map(int, input().split()))
# op_list = []
# for operation, count in zip(['+', '-', '*', '/'], op_count):
#     for i in range(count):
#         op_list.append(operation)

# op_set = set(permutations(op_list, N-1))
# value = []

# for ops in op_set:
#     result = nums[0]
#     for i, op in enumerate(ops):
#         if op == '+':
#             result += nums[i+1]
#         elif op == '-':
#             result -= nums[i+1]
#         elif op == '*':
#             result *= nums[i+1]
#         else:
#             result = int(result / nums[i+1])
#     value.append(result)

# print(max(value))
# print(min(value))


N = int(input())
nums = list(map(int, input().split()))
a, s, m, d = map(int, input().split())

min_value, max_value = 1e9, -1e9


def dfs(i, now):
    global min_value, max_value, a, s, m, d

    if i == N:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if a > 0:
            a -= 1
            dfs(i+1, now + nums[i])
            a += 1
        if s > 0:
            s -= 1
            dfs(i+1, now - nums[i])
            s += 1
        if m > 0:
            m -= 1
            dfs(i+1, now * nums[i])
            m += 1
        if d > 0:
            d -= 1
            dfs(i+1, int(now / nums[i]))
            d += 1


dfs(1, nums[0])
print(max_value)
print(min_value)
