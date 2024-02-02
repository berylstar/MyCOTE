from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
train = [['0' for _ in range(20)] for _ in range(N)]

for _ in range(M):
    order = list(map(lambda x:int(x)-1, input().split()))
    
    if order[0] == 0:
        train[order[1]][order[2]] = '1'
    elif order[0] == 1:
        train[order[1]][order[2]] = '0'
    elif order[0] == 2:
        train[order[1]] = ['0'] + train[order[1]][:19]
    else:
        train[order[1]] = train[order[1]][1:20] + ['0']
        
print(len(set([''.join(i) for i in train])))