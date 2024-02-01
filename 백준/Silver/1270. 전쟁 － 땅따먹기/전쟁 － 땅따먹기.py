from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    d = {}
    line = list(map(int, input().split()))
    max_val = 0
    max_key = 0 
    for i in range(1, len(line)):
        num = int(line[i])
        d[num] = d.get(num, 0) + 1
        if d[num] > max_val:
            max_val = d[num]
            max_key = num

    if max_val > line[0] / 2:
        print(max_key)
    else:
        print('SYJKGW')