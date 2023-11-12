def OddPositive(n):
    s = sum(i*i for i in range(1, n) if i%2 != 0)
    return s
print(OddPositive(10))