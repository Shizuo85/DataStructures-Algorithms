def binary_adder(num1, num2): #this function takes in two binary numbers as arguments and returns their sum 
    if type(num1)!=int or type(num2)!=int: #this checks if the right argument type is inputted
        return "Wrong argument"
    else:
        try:
            num1=int(str(num1),2)       #this converts num1 in binary to its decimmal equivalent 
            num2=int(str(num2),2)       #this converts num1 in binary to its decimmal equivalent
        except:
            return "number must be in base 2" #if an error occurs in the try statement, it means the number isnt expressed in base 2 
        sum_dec=num1+num2               #the sum of the numbers in decimal is stored in sum_dec
        sum_bin=bin(abs(sum_dec))[2:]   #the absolute value of the sum is then converted to binary and stored in sum_bin 
        if sum_dec<0:
            return ("-"+sum_bin)        #if the sum is negative, sum_bin is returned with a minus sign
        else:
            return sum_bin              #if sum is positive, sum_bin is returned unchanged
print(binary_adder(111101,-101))            
