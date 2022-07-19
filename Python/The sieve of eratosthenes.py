def sieve_of_eratos(limit):
    #this function returns a list of all the prime numbers between 1 and the limit entered as parameter
    if(type(limit)!=int or limit<0):  #this ensures that the right argument type is inputted
        return "Limit must be a positive integer"
    else:
        Number_list=[]
        for num in range(2,limit): #this produces a list of all the numbers between 1 and the limit
            Number_list.append(num)
        for i in range(len(Number_list)): #this helps the program access all the indexes of the number_list list
            if(Number_list[i]==0):  #when a number in the list is zero(as a result of the operation below), this tells the loop to skip the number(continue to the next)  
                continue
            else:
                for k in range(i+1, len(Number_list)): #this goes through all the indexes from just after index i till the very end
                    if(Number_list[k]%Number_list[i]==0 and Number_list[k]!=0):
                        #when i is 2, numbers in index 3 till the end are divided by 2, when i is 3, numbers in index 4 till the end are divided by 3, and so on.
                        #when the remainder is 0 and the number divided isnt 0, it is replaced by zero in the list.
                        #Any non-zero number left at the end of the iteration is a prime number
                        Number_list[k]=0
    Prime_list=list(set(Number_list)) #this removes repeated numbers in the list(in this case, just 0)
    Prime_list.sort()#this arranges the elements inthe list in ascending order
    Prime_list.remove(0) #finally the zero is removed to produce a list containing only prime numbers
    return Prime_list
print(sieve_of_eratos(10000))
                        
                        
                
            
            
