def solution(s):
    # return ' '.join(map(lambda x:(x[0].upper() + x[1:].lower()), s.split(" ")))
    return ' '.join([word.capitalize() for word in s.split(" ")])