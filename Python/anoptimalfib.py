def fibonacci(number):
    """
    This funtion takes in an integer number and returns True if the number is part of the sequence and false otherwise
    """
    if type(number)!=int: return "Invalid"
    elif number<0: return "Wrong input"
    elif number==0: return True
    else:
        a, b, i= 1, 0, 1
        while i<=number:  
            b=a
            a=i
            if i==number:return True
            i=a+b
        return False
