def solution(s, skip, index):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in skip:
        alphabet = alphabet.replace(i, '')    
        
    return ''.join(alphabet[(alphabet.index(i) + index) % len(alphabet)] for i in s)