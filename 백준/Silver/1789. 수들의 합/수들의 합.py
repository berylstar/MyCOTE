n = int(input())
summ = 0
result = 0
for i in range(1, n+1):
    summ += i
    result += 1
    
    if summ > n:
        result -= 1
        break
    
print(result)