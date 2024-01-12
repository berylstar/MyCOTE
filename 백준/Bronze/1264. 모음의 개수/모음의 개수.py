import sys
input = sys.stdin.readline

while True:
    strr = input().rstrip()
    
    if strr == '#':
        break
    
    print(sum(strr.upper().count(i) for i in 'AEIOU'))