from sys import stdin
input = stdin.readline

import heapq

for _ in range(int(input())):

    min_q = []
    max_q = []
    numbers = {}

    for _ in range(int(input())):
        msg = input().rstrip()

        if msg == "D 1":
            while True:
                if len(max_q) == 0:
                    break

                temp = -heapq.heappop(max_q)

                if numbers[temp] > 0:
                    numbers[temp] -= 1
                    break
            
        elif msg == "D -1":
            while True:
                if len(min_q) == 0:
                    break

                temp = heapq.heappop(min_q)

                if numbers[temp] > 0:
                    numbers[temp] -= 1
                    break

        else:
            num = int(msg[2:])

            heapq.heappush(min_q, num)
            heapq.heappush(max_q, -num)

            numbers[num] = numbers.get(num, 0) + 1
            
    answer = sorted(num for num in numbers.keys() if numbers[num] > 0)
    
    if not answer:
        print("EMPTY")
    else:
        print(answer[-1], answer[0])