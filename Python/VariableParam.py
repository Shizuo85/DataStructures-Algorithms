def variableParam(*argv):
    """
    This function takes in a variable nuber of binary numbers as sstrings and returns a tuple contaning the elements that are divissible by 5  
    """
    for i in argv:
        assert type(i)==str 
        for k in range(len(i)):
            if k==0: assert i[k]=="-" or i[k]=="0" or i[k]=="1"
            else: assert i[k]=="0" or i[k]=="1"
    lst=[]
    for i in argv:
        if int(i, 2)%5==0:
            if int(i, 2)<0: lst.append(i[1:])
            else: lst.append(i)
    return tuple(lst)

