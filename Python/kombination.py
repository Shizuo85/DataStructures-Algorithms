def power_list(n):
    """
    This function takes in a list and returns the power sets of the list
    """
    lst=[]
    for i in range(len(n)):
        lst.append([n[i]])
        if(i>0):
            for k in range((2**i)-1):#loops through all the indexes before the position of i
                new_list=[n[i]]+lst[k]
                new_list.sort()
                lst.append(new_list) #sums through all the lists before position i
    return lst


def combo(lst, k):
    """
    This function takes in a list of integer and an integer k as input and returns all the k combinations of the list
    """
    assert type(lst)==list and type(k)==int and k>-1 and k<=len(lst)
    for i in lst: assert type(i)==int
    if k==0: return []
    combo_list=[x for x in power_list(lst) if len(x)==k]
    return combo_list


def my_money(arr):
    """
    This function takes in an array of naira notes and returns true if sharing it evenly is possible and false otherwise
    """
    assert (type(arr)==list or type(arr)==set or type(arr)==tuple)
    if type(arr)!=list: arr=list(arr)
    notes=[5, 10, 20, 50, 100, 200, 500, 1000]
    for i in arr: assert i in notes
    if sum(arr)%10!=0: return False
    share=sum(arr)//2; possible_shares=[sum(x) for x in power_list(arr) if len(x)<len(arr)-1]
    if share in possible_shares: return True
    else: return False

