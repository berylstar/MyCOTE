def solution(n):
    if (n**(0.5) % 1 > 0):
        return -1
    else:
        return int(n**(0.5) +1) ** 2