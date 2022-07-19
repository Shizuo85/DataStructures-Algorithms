def order(array):
    """"
    This function takes in an array of integers and returns a tuple containg two elemments.
    The first element of the tuple represents the length of the longest cconsecutive element sequence in the array.
    The second is a sorted list of the remaining elements
    """
    assert type(array)==list, "Invalid input"
    l=1    #length of a sequence
    lst=[] #this list will contain the length of each sequence
    try: array.sort()
    except: return "Invalid input"
    for i in range(len(array)):
        assert type(array[i])==int, "Invalid input"
        try:
            if array[i]+1==array[i+1]:
                l=l+1
            else:
                lst.append(l)
                l=1
        except:  #an index out of range error occurs at the last element
            lst.append(l)
    a=max(lst)                 #this represents the highest number of consecutive elements
    b=sum(lst[0:lst.index(a)]) #this represents the number of elements before the max consecutive element pair
    return (a, array[0:b]+array[a+b:])
print(order([2,1,5,4,6]))
            
