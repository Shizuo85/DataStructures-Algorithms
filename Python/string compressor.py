def compressor(numbers):
    #this function takes in a string of numbers as parameters and returns a tuple containing sub tuples with a number in the string and its number of occurrences as elements
    if(type(int(numbers))!=int or int(numbers)<0):        #this ensures the right argument type is passed into the function
        return "Wrong argument type"
    else:
        number_list=list(numbers)                         #converts the string to a list of each number
        count_list=list(set(number_list))                 #creates another list from the number_list containing all the numbers without repetition.
                                                          #the set method is first used, then it is converted to a list
        count_list.sort()                                 #arranges the values in count_list in increasing order
        tuple_list=[]                                     #this creates an empty list where our tuples will be stored
        for i in range(len(count_list)):                  #this loops through all the indexes in count_list
            count=number_list.count(count_list[i])        #using the count method, each element in count_list is counted in number_list then assigned to count
            tuple_list.append((int(count_list[i]),count)) #then a tuple of the counted number and the count is added to the tuple_list
        return tuple(tuple_list)                          #finally a tuple of the tuple_list is returned
print(compressor("1234567876875654255678089867563452214234568098765"))
print(compressor("0000111122223333444455556666777788889999"))
