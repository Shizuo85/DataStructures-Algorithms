def find_armstrong(start, end):
    """
    This function takes in two integers, a start value and an end value as intervals within which the
    armstrong number is returned as a list, both numbers inclusive. An armstrong number is a number
    that is equal to the sum of the cube of its digits.
    """
    if type(start)!=int or type(end)!=int:
        return "Wrong argument type"
    elif start<0 or end<0 or end<start:
        return "Argument out of range(If both numbers are greater than zero, switch the arguments)"
    else:
        armstrong_numbers=[]         #an empty list which will contain all the armstrong numbers within the interval
        for k in range(start,end+1): #start <= k <= end
            num=str(k)               #the string version of k is assigned to the variable num
            Sum=0
            for m in range(len(num)): 
                Sum=Sum+int(num[m])**3 #each digit in num is cubed and added to the variable sum from left to right
            if k==Sum:
                armstrong_numbers.append(k)
        if len(armstrong_numbers)>0:
            return armstrong_numbers
        else:
            return "There is no armstrong number within the interval"
#print(find_armstrong(1,500))
