def solution(left, right):
    return sum(num if (num ** (0.5) % 1 > 0) else -num for num in range(left, right + 1))