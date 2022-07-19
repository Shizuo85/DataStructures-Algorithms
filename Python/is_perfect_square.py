def is_perfect_square(num):
    """
    This function takes in a number as an integer and returns true if it is a perfect square and false otherise
    """
    if type(num)!=int or num<0:
        return "Invalid input"
    for i in range(0, num//2+2):
        if i*i==num:
            return True
        else:
            continue
    return False
print(is_perfect_square(1))
print(is_perfect_square(225))
print(is_perfect_square(100))
print(is_perfect_square(109))
print(is_perfect_square(49))
print(is_perfect_square(19))
