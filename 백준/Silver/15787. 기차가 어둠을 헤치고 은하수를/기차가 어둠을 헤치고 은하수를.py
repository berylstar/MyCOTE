from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
trains = [0 for _ in range(N)]

for _ in range(M):
    order = list(map(lambda x:int(x)-1, input().split()))
    
    if order[0] == 0:
        trains[order[1]] = trains[order[1]] | (1 << order[2])
    elif order[0] == 1:
        trains[order[1]] = trains[order[1]] & ~(1 << order[2])
    elif order[0] == 2:
        trains[order[1]] = (trains[order[1]] << 1) & ~(1 << 20)
    else:
        trains[order[1]] = trains[order[1]] >> 1
        
print(len(set(trains)))