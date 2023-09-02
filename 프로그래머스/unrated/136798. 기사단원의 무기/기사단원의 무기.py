def solution(number, limit, power):
    number += 1
    dp = [0 for _ in range(number)]
    
    for i in range(1, number):
        for j in range(i, number, i):
            dp[j] += 1
    
    return sum(power if dp[i] > limit else dp[i] for i in range(number))