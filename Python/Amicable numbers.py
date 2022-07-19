def abundant(num):
    """
    This function takes in a positive integer and return the sum of its proper divisors
    """
    Sum=0                    
    for i in range(1,num//2+1):
        if num%i==0:          #this checks if i is a divisor of the num
            Sum=Sum+i         #if it is, it is added to the Sum variable
        else:                 #else the number is skippped
            continue
    return Sum
def amicable(num1, num2):
    """
    This function takes in two positive integers as input parameters and returns True if the sum
    of the proper divisor of each is equal to the other number and False otherwise
    """
    if type(num1)!=int or type(num2)!=int:            #ensures the right argument type is executed
        return "Invalid argument type"
    elif num1<1 or num2<1:                            #ensures only feasible terms are executed
        return "Neither number can be less than 1"
    else:
        if abundant(num1)==num2 and abundant(num2)==num1: #checks if the numbers are amicable
            return True
        else:
            return False
print(amicable(220,284))
            
