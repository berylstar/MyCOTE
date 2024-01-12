import sys
input = sys.stdin.readline

L, P = map(int, input().split())
participants = list(map(int, input().split()))

for participant in participants:
    print(participant-L*P, end=' ')
print()