from sys import stdin
input = stdin.readline

N = int(input())
dna = list(map(str, input().rstrip()))

d = {"AA" : "A", "AG" : "C", "AC" : "A", "AT" : "G", "GA" : "C","GG" : "G",
     "GC" : "T", "GT" : "A", "CA" : "A", "CG" : "T", "CC" : "C", "CT" : "G",
     "TA" : "G", "TG" : "A", "TC" : "G", "TT" : "T"}

a = dna.pop()

while dna:
    a = d[dna.pop()+a]
    
print(a)