def solution(s, n):
    return ''.join(chr((ord(l) - 97 + n)%26 + 97) if l.islower() else (chr((ord(l) - 65 + n)%26 + 65) if l.isupper() else ' ') for l in s)