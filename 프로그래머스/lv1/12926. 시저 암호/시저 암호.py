def solution(s, n):
    small = 'abcdefghijklmnopqrstuvwxyz'
    big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    return ''.join(small[(ord(l) - 97 + n)%26] if l.islower() else (big[(ord(l) - 65 + n)%26] if l.isupper() else ' ') for l in s)