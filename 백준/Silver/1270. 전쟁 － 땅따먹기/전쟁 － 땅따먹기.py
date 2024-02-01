from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    d = {}
    line = list(map(int, input().split()))
    max_val = 0
    max_key = 0 
    for i in range(1, len(line)):
        d[line[i]] = d.get(line[i], 0) + 1
        if d[line[i]] > max_val:
            max_val = d[line[i]]
            max_key = line[i]

    if max_val > line[0] / 2:
        print(max_key)
    else:
        print('SYJKGW')