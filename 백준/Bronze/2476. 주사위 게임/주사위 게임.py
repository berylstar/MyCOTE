import sys
input = sys.stdin.readline

answer = set()

N = int(input())
for i in range(N):
    A, B, C = map(int, input().split())
    
    if A == B == C:
        answer.add(10000 + A * 1000)
    elif A == B:
        answer.add(1000 + A * 100)
    elif B == C:
        answer.add(1000 + B * 100)
    elif C == A:
        answer.add(1000 + C * 100)
    else:
        answer.add(max(A, B, C) * 100)
        
print(max(answer))