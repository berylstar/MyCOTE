from itertools import combinations
def solution(number):            
    return sum(1 for comb in combinations(number, 3) if not sum(comb))