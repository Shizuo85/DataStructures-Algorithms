def unique(L):
    if type(L)!=list: return "Invalid input"
    for i in L:
        if type(i)!=int: return "Invalid input"
        else: continue
    L=list(set(L))
    L.sort()
    return L
print(unique([1,2,3,4,56,6,8,8,9,6,5,46,7,8,65,3,65,43,4,3,55,65,6,5,5]))
