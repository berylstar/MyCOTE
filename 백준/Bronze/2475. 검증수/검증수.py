a, b, c, d, e = map(int, input().split())

print(sum([a*a, b*b, c*c, d*d, e*e]) % 10)