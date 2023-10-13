def GCD(a, b):
    a, b = max(a, b), min(a, b)
    if a % b == 0:
        return b
    else:
        return GCD(b, a%b)
    
def CanDivide(num, array):
    for i in array:
        if i % num == 0:
            return 0
    return num

from functools import reduce
def solution(arrayA, arrayB):            
    return max(CanDivide(reduce(GCD, arrayA), arrayB), CanDivide(reduce(GCD, arrayB), arrayA))