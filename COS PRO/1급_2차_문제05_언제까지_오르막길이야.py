def solution(arr):
	answer = []
	count = 0
	last = arr[0]
	
	for current in arr[1:]:
		if current > last:
			count += 1
		else:
			answer.append(count + 1)
			count = 0
		last = current
	
	answer.append(count + 1)
	return max(answer)
