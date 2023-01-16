def solution(n):
	answer = 0
	
	grid = [[0] * n for _ in range(n)]
	spiral = n // 2
	current = 1
	current_size = n	
	
	for i in range(spiral):
		answer += current
		current += (n - 1) * 2
		answer += current
	
	return answer if n % 2 == 0 else answer + n ** 2
