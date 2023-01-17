def solution(commands):
	answer = [0, 0]
	ways = {
		"L": (-1, 0),
		"R": (1, 0),
		"U": (0, 1),
		"D": (0, -1),
	}
	
	for command in commands:
		for i in range(2):
			answer[i] += ways[command][i]
	
	return answer