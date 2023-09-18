from collections import Counter
def solution(want, number, discount):
    dd = {a:b for a, b in zip(want, number)}
    return sum(1 for i in range(len(discount)-9) if dd == Counter(discount[i:i+10]))