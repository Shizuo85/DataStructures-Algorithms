def max_min(lst):
    for i in range(len(lst)//2):
        lst.insert(i*2, lst.pop(-1))
    return lst
