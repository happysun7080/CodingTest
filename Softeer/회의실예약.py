'''
level: 2/5
'''

import sys
input = sys.stdin.readline


N, M = map(int, input().split())
names, reservations = [], {}
for _ in range(N):
    name = input().rstrip()

    names.append(name)
    reservations[name] = []

for _ in range(M):
    name, start, end = map(str, input().split())
    reservations[name].append((int(start), int(end)))

for index, name in enumerate(sorted(names)):
    table = [0 for _ in range(18 - 9 + 1)]
    result = []
    
    reservations[name].sort()

    last = 0
    for start, end in reservations[name]:
        for i in range(start, end + 1):
            table[i - 9] = 1

        if start - last == 1:
            table[start - 9] += 1

        last = end

    start = 0
    for i, a in enumerate(table):
        if a == 0:
            if start == 0:
                start = i + 9 if i == 0 else i + 8
        else:
            if start != 0:
                result.append((start, i + 9))
                start = 0
            else:
                if i < len(table) - 1 and table[i + 1] == 2:
                    result.append((i + 9, i + 9 + 1))

        if i == len(table) - 1 and start != 0:
            result.append((start, i + 9))

    print("Room", name + ":")
    if not result:
        print("Not available")
    else:
        print(len(result), "available:")
        for start, end in result:
            result_str = str(start) + "-" + str(end)

            if start == 9:
                result_str = "0" + result_str
            
            print(result_str)

    if index < N - 1:
        print("-----")
        
        