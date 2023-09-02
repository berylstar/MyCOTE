def solution(money):
    a, b, c = money[0], money[1], money[0] + money[2]
    d, e, f = 0, money[1], money[2]
    
    for m in money[3:]:
        a, b, c = b, c, max(a, b) + m
        d, e, f = e, f, max(d, e) + m
    return max(a, b, e, f)