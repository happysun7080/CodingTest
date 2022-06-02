### level 2 ###

# 1차: 220523
# 2차: 220603

'''
2022 KAKAO BLIND RECRUITMENT - 주차 요금 계산
'''


import math


def getTime(start, end):
    result_h = 0
    result_m = 0

    if int(start[3:]) < int(end[3:]):
        result_m += int(end[3:]) - int(start[3:])
    else:
        result_m += 60 - (int(start[3:]) - int(end[3:]))
        result_h -= 1
    result_h += int(end[:2]) - int(start[:2])

    return [result_h, result_m]


def getFee(fees, hm):
    if hm <= fees[0]:
        return fees[1]
    else:
        hm_left = hm - fees[0]
        return fees[1] + math.ceil(hm_left / fees[2]) * fees[3]


def solution(fees, records):
    answer = []
    lot = dict()

    for record in records:
        car_num = record[6:10]

        if record[-2:] == "IN":
            if car_num in lot:
                lot[car_num] = [record[:5], lot[car_num][1], 0]
            else:
                lot[car_num] = [record[:5], 0, 0]

        elif record[-3:] == "OUT":
            h, m = getTime(lot[car_num][0], record[:5])
            lot[car_num] = [record[:5], lot[car_num][1] + (h*60 + m), 1]

    for k, v in lot.items():
        if v[2] != 1:
            h, m = getTime(v[0], "23:59")
            answer.append([k, getFee(fees, v[1] + (h*60 + m))])
        else:
            answer.append([k, getFee(fees, v[1])])
    answer.sort()

    return [i[1] for i in answer]


print(solution([180, 5000, 10, 600]["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
      "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))

print(solution([120, 0, 60, 591], ["16:00 3961 IN", "16:00 0202 IN",
                                   "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))

print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
