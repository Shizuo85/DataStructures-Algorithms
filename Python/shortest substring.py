def power_list(n):
    """
    this function takes in a list and returns the power sets of the list 
    """
    if(type(n)!=list):
        return "parameter must be a list"
    else:
        lst=[]
        for i in range(len(n)):
            lst.append([n[i]])
            if(i>0):
                for k in range((2**i)-1):#loops through all the indexes before the position of i
                    lst.append(lst[k]+[n[i]]) #sums through all the lists before position i
        return lst
    
def short_sub(txt, sub):
    """
    This function takes in a word string and a set of letters to find in the string and returnss the shortest ssubstring
    """
    assert type(txt)==str and txt.isalnum() and type(sub)==set
    for i in sub: assert i in txt
    short_sub=[]
    sub_index=[]
    for i in power_list(list(txt)):
        count=0
        for k in sub:
            if k in i: count=count+1
            else: break
        if count==len(sub) and "".join(i) in txt: short_sub.append(i)
    for i in short_sub:
        sub_index.append(len(i))
    return "".join(short_sub[sub_index.index(min(sub_index))])

def selection(lst):
    """
    This function takes in a list and returns the ordered version
    """
    assert type(lst)==list
    for i in lst: assert type(i)==int
    n=0
    for k in range(len(set(lst))):
        a=lst[n]
        for i in range(n+1, len(lst)):
            if a>lst[i]: a=lst[i]
            else: continue
        count=0
        while a in lst:
            lst.remove(a)
            count=count+1
        for i in range(count):
            lst.insert(n, a)
        n=n+count
    return lst

