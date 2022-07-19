def rearrange(lst):
    for i in range(len(lst)):
        if lst[i]<0:
            x=lst.pop(i)
            lst.insert(0, x)
    return lst