number = list(map(int, input()))
answer = [0 for _ in range(10)]
for s in number:
    if s == 6 or s == 9:
        if answer[6] <= answer[9]:
            answer[6] += 1
        else:
            answer[9] += 1
    else:
        answer[s] += 1
print(max(answer))