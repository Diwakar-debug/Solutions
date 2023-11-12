def OddPositive(n):
    s = 0
    for i in range(1, n):
        if i%2 == 0:
            pass
        else:
            s = s + (i*i)
    return s

print(OddPositive(10))