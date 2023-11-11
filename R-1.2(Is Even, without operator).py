def is_even(k):
    is_even = True
    for i in range(1,k+1):
        if is_even == True:
            is_even = False
        else:
            is_even = True
    return(is_even)

print(is_even(19))
