def bits_of_gray(n):
    """
    This function takes in a positive integer as input an returnss list of all the gray code numbers with n as number of digits.
    For a gray code, the first digit is the same as the first digit of its binary equivalent in terms of posiytion. For proceeding digits,
    if the next number in th binary is the same as the current number, 0 is added to the gray code, else 1 is.
    """
    if type(n)!=int or n<1:
        return "Invalid input"
    lst=[]
    for i in range(2**n): #n digits can contain only 2**n gray codes 
        bit=bin(i)[2:]
        gray=bit[0]
        for i in range(1,len(bit)): #first the first digit in binary is compareed  to the next digit and so on till the last
            if bit[i]==bit[i-1]:
                gray=gray+"0"
            else:
                gray=gray+"1"
        if len(gray)<n:
            gray="0"*(n-len(gray))+gray
        lst.append(gray)
    return lst

print(bits_of_gray(3))
