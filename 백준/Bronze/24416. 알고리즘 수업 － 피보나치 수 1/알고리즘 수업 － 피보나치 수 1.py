N = int(input())

fibonacci = [0 for _ in range(N+1)]
fibonacci[1], fibonacci[2] = 1, 1

def Fibonacci(n):
    for i in range(3, n+1):
        fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
    return fibonacci[n]

count1 = Fibonacci(N)
count2 = N-2
print(count1, count2)