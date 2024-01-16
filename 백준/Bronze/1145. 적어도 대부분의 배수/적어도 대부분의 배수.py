from sys import stdin
input = stdin.readline

numbers = list(map(int, input().split()))
answer = min(numbers)
while True:
    count = 0
    for number in numbers:
        if answer % number == 0:
            count += 1
    if count > 2:
        break
    else:
        answer += 1
print(answer)