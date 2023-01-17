from itertools import combinations

def solution(arr, K):
	answer = 0
	combs = list(combinations(arr, K))
	
	for comb in combs:
		if sum(comb) % K:
			continue
		answer += 1
	
	return answer