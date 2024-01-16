from sys import stdin
input = stdin.readline

N = int(input())
answer = list(input().rstrip())

for _ in range(N - 1):    
    for i, w in enumerate(input().rstrip()):
        if answer[i] != w and answer[i] != '?':
            answer[i] = '?'
            
print(''.join(answer))