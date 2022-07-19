def missing_numbers(num_list):
    """
    This function takes in a sorted list and returns another list containing missing numbers from the from list in terms of arithmetic progression
    """
    if type(num_list)!=list:
        return "Wrong input type"
    try:
        #an error occurs when the list contains a tupleor alphanumerics which cant be sorted or when a float begins or ends the sorted list(this affescts the for loop) 
        num_list.sort()
        lst2=[]
        check=0
        for i in range(num_list[0], num_list[-1]): #this loops from the lowest number in the list to the highest
            if type(num_list[check])!=int:
                return "wrong element type"
            elif i==num_list[check]:
                check=check+1
            else:
                lst2.append(i)
        return lst2
    except:
        return "Wrong element type"
print(missing_numbers([-31, 2, 3, 4, 6, 7, 10]))
print(missing_numbers([1, 2, 17, 14, 12, 11, 10]))
print(missing_numbers([1, 2, 3.5, 4, 6, 4]))
