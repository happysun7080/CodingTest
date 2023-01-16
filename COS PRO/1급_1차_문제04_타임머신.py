def solution(num):
	num += 1
	answer = list(map(int, list(str(num))))
	
	for i in range(len(answer)):
		if answer[i] == 0:
			answer[i] = 1
	
	result = 0
	
	for i in range(len(answer)):
		result += answer[::-1][i] * (10 ** i)
	
	return result
