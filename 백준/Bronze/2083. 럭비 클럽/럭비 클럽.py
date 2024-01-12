import sys
input = sys.stdin.readline

while True:
    N, A, W = map(str, input().split())
    
    if N == '#':
        break
        
    print(N, "Senior" if int(A) > 17 or int(W) >= 80 else "Junior")