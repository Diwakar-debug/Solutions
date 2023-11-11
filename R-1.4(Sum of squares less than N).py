def sum_Squares(n):
    sum = 0
    for i in range(1, n):
        square = i*i
        sum += square
    return sum

print(sum_Squares(10))
