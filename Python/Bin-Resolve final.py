dict1={}
def resolve(d, lst):
    """
    This function takes in a dictionary wiith keys and values as positive integers or
    letters and a list with the ssame typpe of elements and returns a resolved list
    using the dictionary keys to values to keys as tokens
    """
    global dict1
    assert type(d)==dict and type(lst)==list
    for k,v in d.items():
        assert (type(k)==str and k.isalpha() or type(k)==int and k>-1)
        assert (type(v)==str and v.isalpha or type(v)==int and v>-1)
    for i in range(len(lst)):
        assert (type(lst[i])==str and lst[i].isalpha() or (type(lst[i])==int and lst[i]>-1))
        dict1={}
        lst[i]=find_in_dict(d,lst[i])
    return lst
def find_in_dict(d, k):
    """
    This function takes in a dictionary and a token to be found in iit and returns the resolved token
    """
    global dict1
    try:
        dict1.setdefault(k, 0)
        dict1[k]=dict1[k]+1
        if dict1[k]>1:
            return k
        else:
            return find_in_dict(d, d[k])
    except:
        return k
def bin(lst1, lst2):
    """
    This function takes in two list and reeturms a third list as the bin of the two.
    The first list is a range of integers and the second list is a list of the lower limts of bins 
    """
    assert type(lst1)==list and type(lst2)==list
    for i in lst1:
        assert type(i)==int
    for k in lst2:
        assert type(k)==int
    if len(lst1)==0: return [0]*len(lst2)
    elif len(lst2)==0: return []
    lst3=[]; lst1.sort(); lst2.sort()
    for i in range(1,len(lst2)):
        n=0
        for k in range(lst2[i-1],lst2[i]):
            if k in lst1: n=n+1
        lst3.append(n)
    n=0
    for m in range(lst2[-1], lst1[-1]+1):
        if m in lst1: n=n+1
    lst3.append(n)
    return lst3
