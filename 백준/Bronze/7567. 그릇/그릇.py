dishes = input()
answer = 10

for i in range(1, len(dishes)):
    if dishes[i - 1] == dishes[i]:
        answer += 5
    else:
        answer += 10
print(answer)