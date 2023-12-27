import sys
input = sys.stdin.readline

H, M, S = map(int, input().split())
D = int(input()) 

S += D
M += S // 60
H += M // 60
print(H%24, M%60, S%60)