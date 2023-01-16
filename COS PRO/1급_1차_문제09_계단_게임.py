def func(record):
	if record == 0:
		return 1
	elif record == 1:
		return 2
	return 0

def solution(recordA, recordB):
	cnt = 0
	for i in range(len(recordA)):
		if recordA[i] == recordB[i]:
			continue
		elif recordA[i] == func(recordB[i]):
			cnt = cnt + 3
		elif cnt > 0:
			cnt = cnt - 1
	return cnt