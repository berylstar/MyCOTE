import sys
input = sys.stdin.readline

while True:
    A, B, C = map(int, input().split())
    
    if A == B == C == 0:
        break
    
    A, B, C = sorted([A, B, C])
    
    if A*A + B*B == C*C:
        print("right")
    else:
        print("wrong")