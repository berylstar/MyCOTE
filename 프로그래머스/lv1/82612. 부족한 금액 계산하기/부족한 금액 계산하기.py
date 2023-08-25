def solution(price, money, count):
    return max(price * sum(range(count+1)) - money, 0)