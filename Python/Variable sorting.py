def var_sort(*argt):
    """
    This function takes in a variable number of tuples and returns a tuplle containing thhe ordered version of the tuple
    """
    lst=[]
    for i in argt:
        assert type(i)==tuple and len(i)==3 and type(i[0])==str and i[0].isalpha() and type(i[1])==type(i[2])==int and i[1]>0 and i[2]>-1
        lst.append(i)
    for i in range(1, len(lst)):
        for k in range(i):
            if lst[i][0]<lst[k][0]:
                    n=lst[i]
                    lst.pop(i)
                    lst.insert(k, n)
                    break
            elif lst[i][0]==lst[k][0]:
                if lst[i][1]<lst[k][1]:
                    n=lst[i]
                    lst.pop(i)
                    lst.insert(k, n)
                    break
                elif lst[i][1]==lst[k][1]:
                    if lst[i][2]<lst[k][2]:
                        n=lst[i]
                        lst.pop(i)
                        lst.insert(k, n)
                        break               
    return lst

