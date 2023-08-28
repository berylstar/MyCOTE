def solution(food):
    strr = ''.join(str(i) * (v // 2) for i, v in enumerate(food))
    return strr + '0' + strr[::-1]