
def solution(r1, r2):
    return sum(int((r2**2 - i**2)**0.5) - int((r1**2 - i**2 - 1)**0.5) if i < r1 else int((r2**2 - i**2)**0.5) for i in range(r2)) * 4