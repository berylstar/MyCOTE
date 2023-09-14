def GCD(a, b):
    [a, b] = [a, b] if a >= b else [b, a]
    if a % b == 0:
        return b
    else:
        return GCD(b, a % b)

def LCM(a, b):
    return a * b // GCD(a, b)

def solution(arr):
    answer = arr[0]
    for i in arr[1:]:
        answer = LCM(answer, i)
    return answer