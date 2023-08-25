def solution(n):
    answer = 0
    while n:
        answer *= 3
        answer += n % 3
        n //= 3
    return answer