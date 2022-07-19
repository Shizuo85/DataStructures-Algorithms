def even_odd(list_num):
    """
    This function takes in a list of integers and prints the number of even and odd numbers in the list
    """
    even, odd=0, 0
    try:                 #try and except clause helps avoid the use of another function to ensure the right input parameter type 
        for i in list_num:
            if type(i)!=int: #function1
                return "Only a list containing integers is allowed"
            elif i%2==0:
                even=even+1
            else:
                odd=odd+1
        print("Number of even numbers is:", even, "\nNummber of odd numbers is:", odd)#function2
    except:
        return "Only a list containing integers is allowed"
even_odd([1,2,3,4,5,6,7,8,9])
