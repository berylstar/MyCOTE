import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
if M:
    broken = set(map(str, input().split()))
else:
    broken = set()

answer = abs(100 - N)

for number in range(1000001):
    if len(set(str(number)) & broken) > 0:
        continue

    answer = min(answer, len(str(number)) + abs(number - N))

print(answer)