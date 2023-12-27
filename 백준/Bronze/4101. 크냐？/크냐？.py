import sys
input = sys.stdin.readline

while True:
    A, B = map(int, input().split())
    
    if A == B == 0:
        break
        
    if A > B:
        print("Yes")
    else:
        print("No")