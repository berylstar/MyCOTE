numbers = list(map(int, input()))

def Multi(arr):
    ret = 1
    for number in arr:
        ret *= number
    return ret

for i in range(1, len(numbers)):
    if Multi(numbers[:i]) == Multi(numbers[i:]):
        print("YES")
        break
else:
    print("NO")