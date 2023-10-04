def IsPrime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

from itertools import permutations
def solution(numbers):
    ans = set()
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            a = int(''.join(j))
            
            if IsPrime(a):
                ans.add(a)
                
    return len(ans)