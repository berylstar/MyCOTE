def GCD(A, B):
    if A % B == 0:
        return B
    else:
        return GCD(B, A % B)
        
def LCM(A, B):
    gcd = GCD(A, B)
    return gcd * (A // gcd) * (B // gcd)

A, B = map(int, input().split())
A, B = max(A, B), min(A, B)
print(GCD(A, B))
print(LCM(A, B))