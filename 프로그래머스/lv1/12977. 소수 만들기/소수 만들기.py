def IsPrime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

from itertools import combinations
def solution(nums):
    return sum(1 for comb in combinations(nums, 3) if IsPrime(sum(comb)))