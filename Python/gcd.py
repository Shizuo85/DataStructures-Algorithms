def gcd(m, n):
    """
    This function takes in two positive integers as input pararmeters
    and returns their greatest common divisor as an integer
    """
    if type(m)!=int or type(n)!=int or m*n==0 or m<0 or n<0:
        return "Invalid argument type"
    for i in range(max(m//2, n//2), 0, -1):
        #the numbers from half of the higher number to 1 is checked for if it is a divisor of both m and n
        #the first number to test true is the gcd, and is returned
        if m%i==0 and n%i==0:
            return i
        else:
            continue
print(gcd(5,15))
