def minmax(digits):
    max = digits[0]
    min = digits[0]

    for i in  digits:
        if i<min:
            min = i
        if i>max:
            max = i
    result(min, max)
    return(result)
digits = input("Enter integers seperated by space: ")
digits = [int(i) for i in digits.split()]
print(minmax(digits))

    
