def bin_search(lst, num):
    #this program return true if a given number is part of a given list, else false 
    lst.sort()
    length= len(lst)
    if(length>1):
        if(lst[length//2]<num):
            lst=lst[length//2:]
            return bin_search(lst,num)
        elif(lst[length//2]>num):
            lst=lst[:length//2]
            return bin_search(lst,num)
        else:
            lst=[lst[length//2]]
            return bin_search(lst,num)
    else:
        if(lst[0]==num):
            return True
        else:
            return False 
#print(bin_search([1,2,3,4,5,6,42,9,72,94,24], 9))
        
