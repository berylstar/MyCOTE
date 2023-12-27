import sys
input = sys.stdin.readline

dots = [0, 0, 0, 0, 0]

for _ in range(int(input())):
    X, Y = map(int, input().split())
    
    if X == 0 or Y == 0:
        dots[4] += 1
    elif X > 0:
        if Y > 0:
            dots[0] += 1
        else:
            dots[3] += 1
    else:
        if Y > 0:
            dots[1] += 1
        else:
            dots[2] += 1

print(f"Q1: {dots[0]}")
print(f"Q2: {dots[1]}")
print(f"Q3: {dots[2]}")
print(f"Q4: {dots[3]}")
print(f"AXIS: {dots[4]}")