import sys
input = sys.stdin.readline

scores = [100, 100]
for i in range(int(input())):
    A, B = map(int, input().split())
    
    if A < B:
        scores[0] -= B
    elif A > B:
        scores[1] -= A
    
print(*scores, sep="\n")