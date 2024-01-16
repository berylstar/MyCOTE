from sys import stdin
input = stdin.readline

N = int(input())
answer = list(input().rstrip())
leng = len(answer)

for _ in range(N - 1):
    word = input().rstrip()
    
    for i in range(leng):
        if answer[i] != word[i] and answer[i] != '?':
            answer[i] = '?'
            
print(''.join(answer))