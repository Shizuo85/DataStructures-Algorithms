def abundant(num):
    """
    This function takes in a positive integer and return True if the sum of its proper divisors is greater
    than the number itself and returns False otherwise
    """
    total=0                   #variable to store the sum of the proper divisors of a number 
    for i in range(1,num//2+1):#loops i from 1 to num//2
        if num%i==0:          #this checks if i is a divisor of the num
            total=total+i     #if it is, it is added to the total variable
        else:                 #else the number is skippped
            continue
    if total>num:             #when the total is greater than the number itself, it is an abundant number, and True is returned
        return True
    else:                     #else False is returned
        return False
def sum_abundant(n):
    """
    This function takes in a positive integer n as input parameter
    and returns the sum of the first n abundant numbers
    """
    if type(n)!=int:                       #ensures the right argument type is executed
        return "Invalid argument type"
    elif n<1:                              #ensures only feasible terms are executed
        return "Enter a feasible term"
    else:
        count, number, Sum=0, 1, 0         #count, number and sum variables are assigned values
        #count is used to count the number of terms added to sum and is assigned 0 since no value has been added
        #number  is the variable passed into the abundant function to check if its an abundant number
        #sum is the variable where the addition of the numbers is stored. it is assigned zero since no values has been added
        while(count!=n): #this loops while the number of terms added to sum is less than n
            if abundant(number): #this reads "if the abundant function returns True for number"
                Sum=Sum+number   #number is added to sum
                count=count+1    #count increases by 1
                number=number+1  #number increases by 1
            else:                #if the abundant function returns False
                number=number+1  #number increases by one
        return Sum               #finally the sum of the numbers is returned
print(sum_abundant(1000))
            
            
