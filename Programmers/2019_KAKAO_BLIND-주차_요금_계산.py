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
    

def solution(fees, records):
    answer = []
    lot = dict()
    
    
    for record in records:
        if record[-2:] == "IN":
            lot[record[6:10]] = [record[:5], 0]
            
        elif record[-3:] == "OUT":
            h, m = 
            
            lot[record[6:10]]
    
    
    
    return answer
