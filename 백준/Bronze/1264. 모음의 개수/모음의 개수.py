import sys
input = sys.stdin.readline

while True:
    strr = input().rstrip()
    
    if strr == '#':
        break
        
    strr = strr.upper()
    
    print(sum(strr.count(i) for i in 'AEIOU'))