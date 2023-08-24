def solution(absolutes, signs):
    return sum(ab if s else -ab for ab, s in zip(absolutes, signs))