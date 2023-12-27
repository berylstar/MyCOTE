import sys
input = sys.stdin.readline

answer = []

N = int(input())
for i in range(N):
    A, B, C = map(int, input().split())
    
    if A == B == C:
        answer.append(10000 + A * 1000)
    elif A == B:
        answer.append(1000 + A * 100)
    elif B == C:
        answer.append(1000 + B * 100)
    elif C == A:
        answer.append(1000 + C * 100)
    else:
        answer.append(max(A, B, C) * 100)
        
print(max(answer))