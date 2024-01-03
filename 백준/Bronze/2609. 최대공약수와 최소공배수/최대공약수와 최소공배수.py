def GCD(A, B):
    if A % B == 0:
        return B
    else:
        return GCD(B, A % B)
        
def LCM(A, B):
    return A * B // GCD(A, B)

A, B = map(int, input().split())
A, B = max(A, B), min(A, B)
print(GCD(A, B))
print(LCM(A, B))