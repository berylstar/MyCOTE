def solution(numbers):
    if sorted(numbers)[-1] == 0:
        return '0'
    return ''.join(sorted(map(str, numbers), key=lambda x:x*4, reverse=True))