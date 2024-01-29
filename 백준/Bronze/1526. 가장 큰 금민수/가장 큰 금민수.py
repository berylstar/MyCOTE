for i in reversed(range(int(input()) + 1)):
    if all((s in '47') for s in str(i)):
        print(i)
        break