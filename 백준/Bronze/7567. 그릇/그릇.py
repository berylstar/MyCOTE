dishes = input()
answer = 10

for i in range(1, len(dishes)):        
    answer += 5 if dishes[i - 1] == dishes[i] else 10
print(answer)