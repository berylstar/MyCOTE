import sys
input = sys.stdin.readline

scores = [100, 100]
for i in range(int(input())):
    A, B = map(int, input().split())
    
    scores[0] -= B if A < B else 0
    scores[1] -= A if A > B else 0
    
print(*scores, sep="\n")