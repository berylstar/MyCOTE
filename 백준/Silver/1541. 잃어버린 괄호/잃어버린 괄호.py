def Plus(strr):
    return sum(map(int, strr.split('+')))

modification = list(map(str, input().split('-')))
answer = Plus(modification[0])
for i in range(1, len(modification)):
    answer -= Plus(modification[i])
print(answer)