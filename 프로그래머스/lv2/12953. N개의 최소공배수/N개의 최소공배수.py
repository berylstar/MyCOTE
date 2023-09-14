def GCD(a, b):
    [a, b] = [a, b] if a >= b else [b, a]
    return b if a % b == 0 else GCD(b, a% b)

def LCM(a, b):
    return a * b // GCD(a, b)

def solution(arr):
    answer = 1
    for i in arr:
        answer = LCM(answer, i)
    return answer