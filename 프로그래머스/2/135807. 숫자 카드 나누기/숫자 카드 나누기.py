def GCD(a, b):
    a, b = max(a, b), min(a, b)
    if a % b == 0:
        return b
    else:
        return GCD(b, a%b)
    
def Divisor(num):
    return [i for i in range(1, num+1) if num % i == 0]

from functools import reduce
def solution(arrayA, arrayB):
    left = Divisor(reduce(GCD, arrayA))
    right = Divisor(reduce(GCD, arrayB))
    
    answer = [0]
    
    for num in left:
        for b in arrayB:
            if b % num == 0:
                break
        else:
            answer.append(num)
            
    for num in right:
        for a in arrayA:
            if a % num == 0:
                break
        else:
            answer.append(num)
            
    return max(answer)