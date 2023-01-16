def solution(pos):
	answer = 0
	col, row = ord(pos[0]) - ord('A'), int(pos[1]) - 1
	ways = [
		(-1, 2),
		(-2, 1),
		(-1, -2),
		(-2, -1),
		(1, 2),
		(2, 1),
		(1, -2),
		(2, -1),
	]
	
	for nx, ny in ways:
		if -1 < col + nx < 8 and -1 < row + ny < 8:
			answer += 1
	
	return answer