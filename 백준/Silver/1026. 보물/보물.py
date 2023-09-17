import sys
input = sys.stdin.readline

N = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()), reverse=True)
answer = 0
for i in range(N):
    answer += A[i] * B[i]
print(answer)