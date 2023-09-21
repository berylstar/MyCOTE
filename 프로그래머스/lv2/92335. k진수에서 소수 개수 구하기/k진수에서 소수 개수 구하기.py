def Kjinsu(num, k):
    st = ""
    while num > 0:
        st = str(num % k) + st
        num //= k
        
    return st

def IsPrime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
        
    return True

def solution(n, k):
    return sum(1 for i in Kjinsu(n, k).split('0') if i and IsPrime(int(i)))