def GCD(a, b):
    if a % b == 0:
        return b
    else:
        return GCD(b, a % b)

def solution(n, m):
    n, m = max(n, m), min(n, m)
    return [GCD(n, m), n * m // GCD(n, m)]